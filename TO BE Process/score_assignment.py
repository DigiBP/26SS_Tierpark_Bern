from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any, Set
import re


# =========================
# 1) DATA MODEL
# =========================

@dataclass
class AssignmentInput:
    """
    Input-Daten für eine einzelne Case-Coach-Kombination.
    Diese Daten entsprechen typischerweise einer Zeile in der Assignment-Tabelle
    bzw. den zusammengeführten Daten aus Case, Coach und Google Maps.
    """
    assignment_id: str
    case_id: str
    coach_id: str

    # Languages: können einzelne oder mehrere Werte enthalten
    # Beispiele:
    # "DE"
    # "DE, IT"
    # "(DE, IT)"
    case_main_language: Optional[str] = None
    case_other_language: Optional[str] = None
    coach_main_language: Optional[str] = None
    coach_other_language: Optional[str] = None

    # Fachlicher Match
    case_type: Optional[str] = None
    coach_skills: Optional[str] = None  # z.B. "Kinderbetreuung,Familienbegleitung"

    # Kapazität und Grösse
    case_size_in_percent: float = 0.0
    coach_remaining_capacity: float = 0.0

    # Dauer in Sekunden aus Google Maps
    duration_value: int = 0


@dataclass
class AssignmentResult:
    """
    Ergebnis der Bewertung für eine Case-Coach-Kombination.
    Dieses Resultat kannst du direkt in deine Assignment-Tabelle zurückschreiben.
    """
    assignment_id: str
    case_id: str
    coach_id: str

    eligible: bool
    exclusion_reason: str

    language_score: int
    duration_score: int
    skill_score: int
    total_score: int


# =========================
# 2) HELPER FUNCTIONS
# =========================

def normalize_text(value: Optional[str]) -> str:
    """
    Vereinheitlicht einen String:
    - None -> ""
    - trimmt Leerzeichen
    - lowercase für robuste Vergleiche
    """
    if value is None:
        return ""
    return value.strip().lower()


def parse_multi_value_field(raw_value: Optional[str]) -> Set[str]:
    """
    Zerlegt Felder mit mehreren Werten in eine saubere Menge.
    Unterstützte Beispiele:
    - "DE"
    - "DE, IT"
    - "(DE, IT)"
    - "DE; IT"
    - " DE , IT "

    Rückgabe:
    - {"de"}
    - {"de", "it"}
    """
    if not raw_value:
        return set()

    # Klammern entfernen
    cleaned = raw_value.strip()
    cleaned = cleaned.replace("(", "").replace(")", "")

    # Auf Komma oder Semikolon splitten
    parts = re.split(r"[;,]", cleaned)

    # Werte bereinigen
    values = {
        normalize_text(part)
        for part in parts
        if normalize_text(part)
    }

    return values


def has_overlap(set_a: Set[str], set_b: Set[str]) -> bool:
    """
    Prüft, ob zwei Mengen mindestens einen gemeinsamen Wert haben.
    """
    return len(set_a.intersection(set_b)) > 0


def parse_skills(skills_raw: Optional[str]) -> Set[str]:
    """
    Skills werden wie Mehrfachwerte behandelt.
    Beispiele:
    - "Kinderbetreuung,Familienbegleitung"
    - "(Kinderbetreuung, Familienbegleitung)"
    """
    return parse_multi_value_field(skills_raw)


# =========================
# 3) HARD CRITERIA
# =========================

def has_language_match(data: AssignmentInput) -> bool:
    """
    Prüft die Sprachlogik auf Basis deiner Regeln.

    Gültige Matches sind:
    1) case_main_language <-> coach_main_language
    2) case_main_language <-> coach_other_language
    3) case_other_language <-> coach_main_language

    Wichtig:
    Sobald mindestens EINE Sprache übereinstimmt, ist das Kriterium erfüllt.
    """
    case_main = parse_multi_value_field(data.case_main_language)
    case_other = parse_multi_value_field(data.case_other_language)
    coach_main = parse_multi_value_field(data.coach_main_language)
    coach_other = parse_multi_value_field(data.coach_other_language)

    return any([
        has_overlap(case_main, coach_main),
        has_overlap(case_main, coach_other),
        has_overlap(case_other, coach_main),
    ])


def violates_hard_criteria(data: AssignmentInput) -> tuple[bool, str]:
    """
    Prüft alle Hard Criteria.

    Hard Criteria:
    H1: Kein gültiger Sprachmatch
    H2: coach_remaining_capacity * 1.2 < case_size_in_percent
    H3: duration_value > 10800

    Wenn eines davon verletzt wird:
    - eligible = False
    - total_score = 0
    """
    # H1: Sprache
    if not has_language_match(data):
        return True, "No valid language match"

    # H2: Restkapazität
    if data.coach_remaining_capacity * 1.2 < data.case_size_in_percent:
        return True, "Insufficient remaining capacity"

    # H3: Dauer
    if data.duration_value > 10800:
        return True, "Travel duration exceeds 10800 seconds"

    return False, ""


# =========================
# 4) SCORING FUNCTIONS
# =========================

def calculate_language_score(data: AssignmentInput) -> int:
    """
    Language Score gemäss deiner Logik:

    L1: case_main_language = coach_main_language -> 30
    L2: case_main_language = coach_other_language -> 15
    L3: case_other_language = coach_main_language -> 15

    Falls mehrere Werte in einem Feld enthalten sind:
    - sobald mindestens eine Sprache passt, gilt die Regel
    - wenn mehrere Regeln gleichzeitig zutreffen, wird der höchste Score genommen
    """
    case_main = parse_multi_value_field(data.case_main_language)
    case_other = parse_multi_value_field(data.case_other_language)
    coach_main = parse_multi_value_field(data.coach_main_language)
    coach_other = parse_multi_value_field(data.coach_other_language)

    scores = []

    # Hauptsprache Case mit Hauptsprache Coach
    if has_overlap(case_main, coach_main):
        scores.append(30)

    # Hauptsprache Case mit Nebensprache Coach
    if has_overlap(case_main, coach_other):
        scores.append(15)

    # Nebensprache Case mit Hauptsprache Coach
    if has_overlap(case_other, coach_main):
        scores.append(15)

    return max(scores) if scores else 0


def calculate_duration_score(duration_value: int) -> int:
    """
    Duration Score auf Basis von duration_value in Sekunden.

    Regeln:
    0 < duration_value <= 1800    -> 30
    1800 < duration_value <= 3600 -> 25
    3600 < duration_value <= 5400 -> 20
    5400 < duration_value <= 7200 -> 15
    7200 < duration_value <= 9000 -> 10
    9000 < duration_value <= 10800 -> 5
    >10800 -> 0 (wird bereits als Hard Criterion ausgeschlossen)
    """
    if duration_value <= 0:
        return 0
    if duration_value <= 1800:
        return 30
    if duration_value <= 3600:
        return 25
    if duration_value <= 5400:
        return 20
    if duration_value <= 7200:
        return 15
    if duration_value <= 9000:
        return 10
    if duration_value <= 10800:
        return 5
    return 0


def has_skill_match(data: AssignmentInput) -> bool:
    """
    Prüft, ob case_type in coach_skills enthalten ist.

    Beispiel:
    case_type = "Kinderbetreuung"
    coach_skills = "Kinderbetreuung,Familienbegleitung"

    -> True
    """
    case_type = normalize_text(data.case_type)
    coach_skills = parse_skills(data.coach_skills)

    return case_type in coach_skills


def calculate_skill_score(data: AssignmentInput) -> int:
    """
    Skill Score:
    case_type = coach_skills -> 40
    sonst -> 0
    """
    return 40 if has_skill_match(data) else 0


# =========================
# 5) MAIN SCORING FUNCTION
# =========================

def score_assignment(data: AssignmentInput) -> AssignmentResult:
    """
    Führt die komplette Bewertung für genau eine Assignment-Zeile durch.

    Ablauf:
    1. Hard Criteria prüfen
    2. Falls verletzt -> Score 0
    3. Sonst Teil-Scores berechnen
    4. Gesamtscore bilden
    """
    violates, reason = violates_hard_criteria(data)

    if violates:
        return AssignmentResult(
            assignment_id=data.assignment_id,
            case_id=data.case_id,
            coach_id=data.coach_id,
            eligible=False,
            exclusion_reason=reason,
            language_score=0,
            duration_score=0,
            skill_score=0,
            total_score=0,
        )

    language_score = calculate_language_score(data)
    duration_score = calculate_duration_score(data.duration_value)
    skill_score = calculate_skill_score(data)

    total_score = language_score + duration_score + skill_score

    return AssignmentResult(
        assignment_id=data.assignment_id,
        case_id=data.case_id,
        coach_id=data.coach_id,
        eligible=True,
        exclusion_reason="",
        language_score=language_score,
        duration_score=duration_score,
        skill_score=skill_score,
        total_score=total_score,
    )


# =========================
# 6) OPTIONAL HELPER FOR MAKE / API
# =========================

def score_assignment_from_dict(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Hilfsfunktion, falls du später JSON aus Make oder Camunda erhältst.

    Beispiel:
    payload = {
        "assignment_id": "CASE001-COACH001",
        ...
    }

    Rückgabe:
    Dictionary mit allen Resultatfeldern
    """
    data = AssignmentInput(
        assignment_id=str(payload.get("assignment_id", "")),
        case_id=str(payload.get("case_id", "")),
        coach_id=str(payload.get("coach_id", "")),
        case_main_language=payload.get("case_main_language"),
        case_other_language=payload.get("case_other_language"),
        coach_main_language=payload.get("coach_main_language"),
        coach_other_language=payload.get("coach_other_language"),
        case_type=payload.get("case_type"),
        coach_skills=payload.get("coach_skills"),
        case_size_in_percent=float(payload.get("case_size_in_percent", 0)),
        coach_remaining_capacity=float(payload.get("coach_remaining_capacity", 0)),
        duration_value=int(payload.get("duration_value", 0)),
    )

    result = score_assignment(data)
    return asdict(result)


# =========================
# 7) LOCAL TEST
# =========================

if __name__ == "__main__":
    example_payload = {
        "assignment_id": "CASE001-COACH001",
        "case_id": "CASE001",
        "coach_id": "COACH001",
        "case_main_language": "(DE, EN)",
        "case_other_language": "IT",
        "coach_main_language": "(DE, FR)",
        "coach_other_language": "IT",
        "case_type": "Kinderbetreuung",
        "coach_skills": "(Kinderbetreuung, Familienbegleitung)",
        "case_size_in_percent": 30,
        "coach_remaining_capacity": 50,
        "duration_value": 4147,
    }

    result = score_assignment_from_dict(example_payload)
    print(result)
    
