from flask import Flask, request, jsonify
from score_assignment import score_assignment_from_dict

app = Flask(__name__)


@app.route("/", methods=["GET"])
def healthcheck():
    """
    Einfacher Test-Endpunkt, um zu prüfen, ob die API läuft.
    """
    return jsonify({
        "status": "ok",
        "message": "Scoring API is running"
    })


@app.route("/score-assignment", methods=["POST"])
def score_assignment_endpoint():
    """
    Nimmt Assignment-Daten als JSON entgegen,
    berechnet den Score und gibt das Ergebnis als JSON zurück.
    """
    try:
        payload = request.get_json()

        if not payload:
            return jsonify({
                "error": "No JSON payload received"
            }), 400

        result = score_assignment_from_dict(payload)

        return jsonify(result), 200

    except Exception as e:
        return jsonify({
            "error": "Internal server error",
            "details": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
