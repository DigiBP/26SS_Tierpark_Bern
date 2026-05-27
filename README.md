# TO-BE BPMN Camunda Model: Case Allocation Process



# Team Members

| Name | Email |
|------|-------|
| Cedric Iseli | cedric.iseli@students.fhnw.ch|
| Dionis Mrlaku| dionis.mrlaku@students.fhnw.ch|
| Kanika Mukhija|kanika.mukhija@students.fhnw.ch |
| Pallavi Gowda| pallavi.gowda@students.fhnw.ch |
| Shakunthala Reddy Patlolla|shakunthalareddy.patlolla@students.fhnw.ch  |

# Supervisors

1. Charuta Pande
2. Andreas Martin
2. Devid Montecchiari

# Introduction

This document describes the Case allocation process at Changekultur organization as part of the “Digitilaization of Businesss Processes” project at the University of applied Sciences and Arts North-Western Switzerland. The purpose of this process is to reduce manual effort, improve transparency, and support better decision-making during coach allocation. 

# Description of the Use Case 


In the digital age, manual and informal allocation processes can become time-consuming, inconsistent, and difficult to monitor. For our project, we are inspired by  ChangeKultur GmbH, a Zürich‑based social services organization, that provides family coaching, youth support, and integration programs across Switzerland. The company focuses on empowering families through structured coaching and multilingual support. 

One of the processes that required attention was the case allocation process. When a new client case is received, the organisation needs to identify and assign the most suitable Family Coach within a short period of time. In the current situation, this decision is largely manual and depends on the Case Coach’s personal knowledge of available coaches. This makes the process time-intensive and increases the risk of subjective decisions, incomplete information, and delays. 

Our digital solution aims to streamline and automate the case allocation process. Our solution uses Camunda to model and control the workflow and Make to support automation and system integration. This improves transparency, reduces manual effort, and ensures that the allocation decision is supported by structured data while still keeping human judgement in the final decision. This is important because family coach allocation should not only be based on system scores, but also on professional judgement and the specific needs of the family. 

There is no automation in the current ChangeKultur case allocation process. Therefore, our group created a AS-IS BPMN process based on the information available, identified the main pain points, and designed a TO-BE process that introduces automation, scoring, review steps, and error handling for a more reliable and transparent case allocation process.

**Out of scope**: This project does not include a full production system, real integration with company databases, live availability checking of Family Coaches, a mobile app, advanced AI matching, or full client communication. If no suitable Family Coach is available, the case is not processed further in this process. The project is only a prototype to support case allocation, and the final decision will still be made by the Case Coach.


-------------------------------------------------------------------------------------------------------------------------------------------

# AS-IS Process: Case Allocation


## BPMN AS-IS Process
<img width="1945" height="657" alt="image" src="https://github.com/user-attachments/assets/9e110d55-5a47-45c9-b5b5-c9ce13664917" />


# Current Situation

The AS-IS Case Allocation process begins once a case is enquired and is ready for further handling. The Case Coach first reviews the case requirements, including the client’s needs, support intensity, language requirements, geographic location, and any specific experience or specialization needed. Based on this assessment, the Case Coach identifies potentially suitable Family Coaches using available case information and personal knowledge of the team. 

The Case Coach then evaluates the suitability of the identified Family Coaches and informally checks their actual availability. This step is carried out through direct communication and relies heavily on experience, tacit knowledge, and practical understanding of each coach’s current workload, willingness, and personal situation. Since no centralized allocation system exists, the process depends on fragmented information from Microsoft Dynamics, Teams, email, phone communication, and informal notes, making the assessment largely manual and judgment-based. 

If a suitable and available Family Coach is confirmed, the Case Coach selects the most appropriate candidate, informs the Family Coach, and proceeds with assigning the case. The client is then informed, and the process ends with the case allocated. If no suitable coach is available, the process ends without allocation. Overall, the AS-IS process is flexible but highly dependent on manual coordination and individual expertise, which results in limited transparency, inconsistent decision-making, and reduced scalability. 



# AS-IS Pain Points


**Manual case handling** 
The responsible person must manually collect and compare all information needed for the assignment. 

**Time-consuming coach selection** 
Finding a suitable family coach can take time, especially if several coaches need to be checked. 

**Limited transparency**
It is difficult to clearly track why a specific coach was selected or rejected. 

**No automated distance calculation**
Distance or travel time between the client and possible family coaches is not automatically calculated. 

**No suitability criteria**
there is no way to identify a suitable coach for a given case. Suitability decisions depend on personal judgment. 

**Inconsistent decision-making**
Since there are no standardized criteria or scoring logic, similar cases may be allocated differently by different Case Coaches. 


# TO-BE Process: Case Allocation


## BPMN TO-BE Process



<img width="6219" height="2418" alt="To-Be_Case_Allocation_66_Backup_final_v6" src="https://github.com/user-attachments/assets/03293e3d-c688-4532-8544-c40e77615669" />








## Description of the TO-BE Process Elements 






| Row | BPMN Element | Description | Comment |
|---|---|---|---|
| 1 | <img width="80" height="87" alt="image" src="https://github.com/user-attachments/assets/7099b190-707d-4b91-87e6-878dd571a611" /> | The process starts when a new case is received, and the administrator initiates the allocation workflow. | This represents the formal beginning of the case allocation process. |
| 2 | <img width="134" height="106" alt="image" src="https://github.com/user-attachments/assets/27c5da3d-4404-4b73-a65c-ed7f3b91fa9d" /> | The administrator enters the client’s case information into a structured digital form. This includes relevant details such as name, address, language, case type, and other related attributes. | This replaces unstructured manual data collection and ensures standardized and reusable client data. |
| 3 | <img width="131" height="121" alt="image" src="https://github.com/user-attachments/assets/b4829713-4c6b-4dec-a3fc-6b2a32e5af94" />| The system automatically retrieves available coach data and calculates objective matching criteria, such as travel distance, language compatibility, and other hard factors. It then generates an initial ranking or score for possible coaches. | This is the main automation step and supports efficient, data-driven preselection of suitable family coaches. |
| 4 | <img width="50" height="45" alt="image" src="https://github.com/user-attachments/assets/dee72df9-e726-4806-a486-0ce3026dbb52" />| The boundary error event captures technical or data-related failures occurring during the automated allocation step, such as API errors, missing data, or unsuccessful service execution. | This ensures that automation failure does not terminate the entire process and that exception handling is explicitly modeled. |
| 5 | <img width="141" height="112" alt="image" src="https://github.com/user-attachments/assets/5c39f7cd-267f-4c97-9cb0-2f03910755c5" /> | If the automated allocation is unsuccessful, the Case coach manually reviews the case, handles the exception, and assigns a suitable family coach based on the available information and professional judgment. | This user task serves as the fallback for exception scenarios, ensuring human oversight and process continuity when automation cannot produce a valid result. |
| 6 | <img width="125" height="104" alt="image" src="https://github.com/user-attachments/assets/f1f8b613-67a1-4f5c-ba0c-acb4db9b5a2b" /> | The system consolidates the automated calculation results and prepares a shortlist of candidate coaches for further review. | This structures the output of the automated scoring step and makes it usable for further decision-making. |
| 7 | <img width="130" height="102" alt="image" src="https://github.com/user-attachments/assets/1db90d78-7b89-42ee-aef6-41ef50239ec4" /> | The responsible person reviews the automatically generated shortlist and checks whether the proposed assignments are plausible and operationally acceptable. | This keeps human control in the process before moving to the qualitative evaluation stage. |
| 8 | <img width="138" height="111" alt="image" src="https://github.com/user-attachments/assets/073f1d5e-dc67-4c4c-ae58-da9867c20a9e" /> | The system evaluates qualitative suitability criteria using decision logic, such as case complexity, coach experience, and coach type. This produces a recommendation result for the shortlisted coach. | This step introduces decision automation through DMN while still supporting human judgment. |
| 9 | <img width="128" height="103" alt="image" src="https://github.com/user-attachments/assets/4fee0860-1765-4b0d-8d61-e008789f1958" /> | The Case Coach reviews the selected coach profile and the soft-factor evaluation result to assess whether the proposed match is appropriate. | This ensures that the final recommendation is validated by a human expert and reflects the real practice of coach allocation, ensuring that the coach is suitable for a specific case. |
| 10 | <img width="93" height="94" alt="image" src="https://github.com/user-attachments/assets/483498ca-67cb-413f-941a-c9289a7e21d0" /> | This decision point checks whether the selected coach is considered suitable based on the preceding evaluation and human review. | If the coach is recommended, the process continues to client communication. If not, the process loops back to evaluate another option. |
| 11 | <img width="136" height="110" alt="image" src="https://github.com/user-attachments/assets/ebce77cc-4cb1-4680-95d5-f948e9f5298f" /> | The client is informed about the allocation result. | This is the final communication step before process completion. |
| 12 | <img width="89" height="85" alt="image" src="https://github.com/user-attachments/assets/a857950a-bb2a-4294-9753-86d439eefff4" /> | The process ends once the case has been successfully allocated and the client has been informed. | This marks the successful completion of the TO-BE allocation process. |
| 13 | <img width="133" height="107" alt="image" src="https://github.com/user-attachments/assets/3ae41774-4634-4485-92f4-616bd151bd73" /> | Notify the client about the non assignment. | This is the final communication step before process completion.|
| 14 | <img width="110" height="80" alt="image" src="https://github.com/user-attachments/assets/583ffd51-71fe-4343-be6f-b34d1c16a819" /> | The process ends once the case has not been successfully allocated and the client has been informed. | This marks the completion of the TO-BE allocation process. |




## 1. Description 


The TO-BE process represents a significant step towards a more digitalized and automated **Case Allocation** process. The goal of the project team was to automate time-consuming, frequently occurring and rule-based tasks that directly address the main pain points of the company. The collected pain points and the visualized As-Is process formed the foundation for designing the To-Be process.

The use case focuses on allocating a client case to the most suitable Family Coach. The process begins when the admin enters the client data through a structured form. This information is stored in the `unassigned_cases` table in the database. After the client data has been submitted, the system automatically calculates distance and scoring information for potential Family Coaches. The calculation is based on hard factors such as workload, language requirements, location and coach profile information.

The calculated results are stored in the `assignments` table for each individual case-coach combination. The Admin then reviews the generated assignments before the process moves to the Case Coach. Once an assignment is available, the Case Coach evaluates additional soft factors, such as case complexity, coach experience and coach type. After this evaluation, the Case Coach reviews the Family Coach profile and decides whether the recommended coach is appropriate.

If an error occurs during the automated calculation or assignment generation, the process is routed to a manual step. In this exception path, the Case Coach reviews the error and manually selects an alternative coach. For this manually selected coach, the soft factors are evaluated again before the process continues.

If the coach is recommended and accepted, the client is informed about the allocation and the case is marked as assigned. If the coach is not recommended, the process returns to the soft factor evaluation step so that another assignment can be reviewed.

Compared to the AS-IS process, the TO-BE process contains fewer manual tasks and introduces several automated system tasks. This improves efficiency, reduces manual coordination effort and creates a more structured and transparent basis for decision-making. At the same time, human judgement remains part of the process, especially when reviewing assignment suggestions and evaluating soft factors.

---

## 2. Criteria for Task Automation

Before designing the TO-BE process, the project team evaluated which tasks were suitable for automation. The goal was not to automate the entire process blindly, but to identify tasks where automation creates real business value.

The following criteria were used to assess the automation potential of process tasks:

| Criterion | Evaluation Question | Automation Potential |
|---|---|---|
| Standardization | Is the degree of standardization high enough? Are the inputs and outputs fixed? | High, if the task follows a stable and repeatable structure. |
| Rule-based Logic | Is the process rule-based, or does it require human judgement? | High, if clear business rules can be defined. |
| Digital Input | Are the required inputs available in a readable digital format? | High, if data is already structured and digitally available. |
| Volume and Manual Effort | How time-consuming is the process? How high is the transaction volume? | High, if the task is repetitive and manually intensive. |
| Dependencies and Limitations | Are there dependencies or technical limitations that prevent automation? | Low, if many external dependencies or unclear data structures exist. |
| Risk | Which process risks require manual work or human validation? | Low, if incorrect automation could create significant operational risks. |
| Probability of Upgrades | Will the underlying system be maintained or replaced shortly? | Low, if the system landscape is unstable or temporary. |

Source: FHNW Course BPM Slides 2025

The Case Allocation process was considered suitable for automation because several activities are repetitive, data-driven, rule-based and based on structured input data.



## 3. Overview involved systems: Make, Camunda, Google Form, Google Sheet, Flask API

<img width="1801" height="1152" alt="CaseAllocation Systemcontext drawio" src="https://github.com/user-attachments/assets/544adaed-5df3-4871-a283-cb45146250e1" />



The high-level architecture shows how the TO-BE Case Allocation process is supported by different technical components and automation tools.

The process starts with the submission of client data through a Google Form. The data is stored in the `unassigned_cases` table and then processed through Make scenarios. Make acts as the central integration layer between Google Sheets, Camunda, Google Maps, the Flask API and the Python scoring logic.

The Flask API provides access to the Python scoring script, which calculates the suitability score for each case-coach combination. The Google Maps API is used to calculate travel distance and driving duration. The results are stored in the `assignments` table.

Camunda coordinates the overall workflow. It triggers Make scenarios, manages user tasks such as claiming, completing and reviewing tasks, and supports the final decision-making process. The Camunda Cockpit is used to monitor and manage the process execution.



---

## 4. Main Changes in the TO-BE Process

### 4.1 Creation of a New Database Structure

A new database structure was created using Google Sheets. The database consists of three main tables:

| Table | Purpose |
|---|---|
| `unassigned_cases` | Stores newly entered client cases that still need to be allocated. |
| `coaches` | Stores all relevant coach information, including languages, skills and capacity. |
| `assignments` | Stores calculated case-coach combinations, including distance, duration, eligibility and scoring results. |

This structure allows the process to store and process all relevant information in a structured way.

Additional data fields were introduced so that the company has more information available for automated decision support. These fields include languages, case type, workload, coach skills, coach capacity, case complexity and travel duration.

---

### 4.2 Structured Data Collection Through an Onboarding Form

An Onboarding form was created to ensure that new case data is collected in a consistent and structured format.

The form helps to standardize the input data and reduces the risk of missing or inconsistent information. Once submitted, the data is stored in the `unassigned_cases` table and can be used by the automated workflow.

This is important because automation requires readable and structured digital input. Without standardized input data, the later calculation of distances, eligibility and scores would not be reliable.

---

### 4.3 Integration of the Google Maps API

The Google Maps API is used to automatically calculate the travel distance and estimated driving duration between the client address and the coach address.

The calculated values are stored in the `assignments` table.

| Field | Description |
|---|---|
| `distance_text` | Human-readable distance, for example `49.6 km`. |
| `distance_value` | Distance in meters. |
| `duration_text` | Human-readable driving duration, for example `45 mins`. |
| `duration_value` | Driving duration in seconds. |

This automation replaces manual distance checks and ensures that every possible case-coach combination is evaluated consistently.

---

### 4.4 Flask API and Python Scoring Script

A Flask API was created to make the Python scoring logic accessible from Make.

The Flask API exposes the following endpoint:

```http
POST /score-assignment
```

Make sends one case-coach combination to this endpoint. The Python script then calculates the eligibility and score for the assignment.

The scoring logic considers the following criteria:

| Scoring Area | Description |
|---|---|
| Language Match | Checks whether the client and coach have compatible languages. |
| Capacity | Checks whether the coach has enough remaining capacity. |
| Travel Duration | Checks whether the travel duration is acceptable. |
| Skill Match | Checks whether the coach has the required skills for the case type. |

The result is returned to Make and written back into the `assignments` table.

---

## 5. Data Model

### Entity Relationship Diagramm / ERD

<img width="801" height="1031" alt="Datenmodel DigiBP drawio" src="https://github.com/user-attachments/assets/a2fec0a0-ba14-49e7-b68d-75e3fcffd224" />


Since the prototype uses Google Sheets as a lightweight database, some case and coach attributes are stored redundantly in the `assignments` table. In a fully normalized relational database, these attributes would normally be retrieved through the foreign keys `case_id` and `coach_id`. However, for the Google Sheets and Make-based prototype, storing these values as snapshot data makes the assignment results easier to review, export and process in subsequent automation steps.

### 5.1 Table: `unassigned_cases`

The `unassigned_cases` table stores client cases that have not yet been fully allocated.

| Field | Description |
|---|---|
| `case_id` | Unique case identifier |
| `First Name` | Client first name |
| `Last Name` | Client last name |
| `Address` | Client street address |
| `City` | Client city |
| `Postal Code` | Client postal code |
| `Main Language` | Client main language |
| `Other Language` | Additional client language |
| `Urgency` | Urgency of the case |
| `Type` | Case type |
| `Workload` | Expected workload or case size |
| `Zeitstempel` | Timestamp of the case entry |
| `Case Complexity` | Complexity of the case |
| `camunda_submitted` | Indicates whether the case was already submitted to Camunda |
| `assigned` | Indicates whether assignment calculation was already triggered |

---

### 5.2 Table: `coaches`

The `coaches` table stores all available family coaches.

| Field | Description |
|---|---|
| `coach_id` | Unique coach identifier |
| `first_name` | Coach first name |
| `last_name` | Coach last name |
| `address` | Coach street address |
| `postal_code` | Coach postal code |
| `city` | Coach city |
| `main_language` | Coach main language |
| `other_language` | Additional coach language |
| `skills` | Coach skills |
| `active` | Indicates whether the coach is active |
| `workload` | Current workload |
| `capacity_max_in_prozent` | Maximum capacity |
| `remaining_capacity` | Remaining available capacity |
| `coach_experience` | Experience level |
| `coach_type` | Coach employment type |

---

### 5.3 Table: `assignments`

The `assignments` table stores one calculated row per case-coach combination.

| Field | Description |
|---|---|
| `assignment_id` | Unique assignment ID composed of case ID and coach ID |
| `case_id` | Linked case |
| `coach_id` | Linked coach |
| `coach_first_name` | Coach first name |
| `coach_last_name` | Coach last name |
| `coach_main_languages` | Coach main languages |
| `coach_other_languages` | Coach other languages |
| `coach_skills` | Coach skills |
| `coach_remaining_capacity` | Remaining coach capacity |
| `coach_city` | Coach city |
| `case_first_name` | Client first name |
| `case_last_name` | Client last name |
| `case_size_in_procent` | Case workload or size |
| `case_urgency` | Case urgency |
| `case_main_languages` | Case main languages |
| `case_other_languages` | Case other languages |
| `case_type` | Type of case |
| `case_city` | Case city |
| `distance_text` | Human-readable distance |
| `distance_value` | Distance in meters |
| `duration_text` | Human-readable travel duration |
| `duration_value` | Duration in seconds |
| `status` | Processing status |
| `created_at` | Timestamp of assignment creation |
| `eligible` | Indicates whether the coach is eligible |
| `exclusion_reason` | Reason if the coach is not eligible |
| `language_score` | Score for language match |
| `duration_score` | Score for travel duration |
| `skill_score` | Score for skill match |
| `total_score` | Total calculated score |
| `coach_experience` | Coach experience level |
| `case_complexity` | Complexity of the case |
| `coach_type` | Coach type |

---

## 6. Detailed Process Description

### Step 1: Enter Client Data Forms

The process starts with a user task where the administration enters the client and case data into a Google Form `Onboarding Details` [Link](https://docs.google.com/forms/d/e/1FAIpQLScMQjz-gnmlCsyXJdbgRhEz9PHKRcYQhKztVMIKHRDN2gxzEA/viewform). This includes personal data, address data, languages, urgency, case type, workload and case complexity.

The entered data can then be submitted and the data is directly stored in the `unassigned_cases` Google Sheet from the Google-Doc `Data Base Client`



#### Related Make Scenario: Get Onboarding Data

The Make scenario **Get Onboarding Data** reads new cases from `unassigned_cases`.
<img width="748" height="294" alt="Make Get Onboarding Data" src="https://github.com/user-attachments/assets/fe4a38e4-f045-4015-9769-6225a276fe75" />


The scenario filters for rows where `camunda_submitted` is still empty. It then sends the case information to the Camunda `submit-form` endpoint for the process `CaseAllocation66`.

The JSON sent to Camunda includes variables such as:

```json
{
  "caseId": "...",
  "firstName": "...",
  "lastName": "...",
  "address": "...",
  "city": "...",
  "postalCode": "...",
  "mainLanguage": "...",
  "otherLanguage": "...",
  "urgency": "...",
  "caseType": "...",
  "workload": "...",
  "case_complexity": "..."
}
```

After successful submission, the case is marked as submitted in Google Sheets by setting:

```text
camunda_submitted = TRUE
```

---

### Step 2: Calculate Distances and Score

The task **Calculate Distances and Score** is an automated service task.

Its purpose is to generate possible coach assignments for an unassigned case. For each available coach, the process calculates the travel distance and travel duration from the coach address to the client address. Afterwards, the system evaluates whether the coach is suitable for the case.

The output of this step is a set of assignment rows in the `assignments` table [Link](https://docs.google.com/spreadsheets/d/1wtEg8CzwnzGQjX8aDpIscO8urUH8aX7tE8-TYz_ERgA/edit?gid=425397286#gid=425397286).

#### Related Make Scenario: Calculate Distances and Score

<img width="1490" height="287" alt="Make Calculate Distances and Score" src="https://github.com/user-attachments/assets/9e5ec88b-8255-4ca7-a6df-89692cff43d2" />


This scenario is triggered by a Make webhook from Camunda. It performs the following logic:
![alt text](image-1.png)

1. Receive trigger from Camunda.
2. Search for unassigned cases in `unassigned_cases`.
3. Mark the case in the `unassigned_cases`in the field `assigned` = `TRUE` 
4. Read available coaches from the `coaches` table.
5. Calculate distance and duration with Google Maps.
6. Add one row per case-coach combination to the `assignments` table.
7. Call the Flask API endpoint `/score-assignment`.
8. Write the returned scoring result back to the assignment row.
9. Return a response to Camunda.

#### Google Maps Calculation


For each possible case-coach combination, the Make scenario calls the **Google Maps Distance Matrix API** through the Google Maps module. The API is used to calculate the travel distance and travel duration between the coach and the client.

The scenario builds the API request based on address attributes from the `coaches` and `unassigned_cases` tables:

| API Input   | Source Table       | Used Attributes                      |
| ----------- | ------------------ | ------------------------------------ |
| Origin      | `coaches`          | Coach address, postal code and city  |
| Destination | `unassigned_cases` | Client address, postal code and city |
| Travel mode | Fixed value        | Driving                              |
| Units       | Fixed value        | Metric                               |

The Google Maps API then returns the calculated route information. These returned values are written back into the newly created assignment row in the `assignments` table. This means that every generated assignment contains not only the case and coach data, but also the travel distance, travel duration and Google Maps status for this specific combination. This is consistent with the Make blueprint, where the Google Maps module uses the coach address as origin and the client address as destination, and the returned distance and duration values are stored in the `assignments` table. 

For each coach, Google Maps returns:

| Output           | Description                                    |
| ---------------- | ---------------------------------------------- |
| `distance.text`  | Human-readable distance, for example `49.6 km` |
| `distance.value` | Distance in meters                             |
| `duration.text`  | Human-readable duration, for example `45 mins` |
| `duration.value` | Duration in seconds                            |
| `status`         | Google Maps result status                      |

These values are stored in the `assignments` table and are later used as input for the scoring logic. In particular, `duration.value` is passed to the Flask API endpoint `/score-assignment`, where it is used to evaluate whether the coach is suitable for the case and to calculate the duration score.



#### Assignment Row Creation

The scenario creates one assignment row per case-coach combination.

The `Add a Row` module writes values such as:

```text
assignment_id = case_id + "-" + coach_id
case_id
coach_id
coach_first_name
coach_last_name
coach_main_languages
coach_other_languages
coach_skills
coach_remaining_capacity
coach_city
case_first_name
case_last_name
case_size_in_procent
case_urgency
case_main_languages
case_other_languages
case_type
case_city
distance_text
distance_value
duration_text
duration_value
status
created_at
coach_experience
case_complexity
coach_type
```

#### Flask API Scoring

After the assignment row has been created, Make calls the Flask API:

```http
POST /score-assignment
Content-Type: application/json
```

Example payload:

```json
{
  "assignment_id": "CASE-0002-COACH001",
  "case_id": "CASE-0002",
  "coach_id": "COACH001",
  "case_main_language": "German",
  "case_other_language": "French",
  "coach_main_language": "German",
  "coach_other_language": "French",
  "case_type": "Medium",
  "coach_skills": "Kinderbetreuung,Familienbegleitung",
  "case_size_in_percent": 20,
  "coach_remaining_capacity": 80,
  "duration_value": 2703
}
```

Example response:

```json
{
  "assignment_id": "CASE-0002-COACH001",
  "case_id": "CASE-0002",
  "coach_id": "COACH001",
  "eligible": true,
  "exclusion_reason": "",
  "language_score": 30,
  "duration_score": 25,
  "skill_score": 0,
  "total_score": 55
}
```

The returned values are written back into the score columns of the same assignment row.

---


### Step 3: Boundary Error Event

The Boundary Error Event captures technical, integration, and data-related exceptions that may occur during the automated service task. Possible errors include failures in Google Maps distance calculation, Google Sheets data retrieval, Make scenario execution, HTTP/API requests, authentication, missing or invalid input data, webhook communication, timeouts, and unsuccessful system calculations. When such an error occurs, the process is redirected to a fallback path instead of stopping completely. This allows the Case Coach to review the case and continue the case allocation manually, ensuring process continuity and human oversight when automated execution is not possible.


### Step 4: Assign Manually 

Assign Manually is a User Task that is performed when the automated allocation cannot be completed successfully. This may happen because of missing or inconsistent data, technical or integration issues. 

In this step, the Case Coach takes over the process manually and reviews the case, identifies the issue that prevented the automated allocation, and decides how to proceed. Based on the available case information, workload data, and professional judgment, the Case Coach manually selects a suitable Family Coach. 

The purpose of this task is twofold. First, it provides human error handling by ensuring that technical, data-related, or system-related problems are reviewed instead of blocking the process. Second, it serves as a manual fallback that allows the case allocation process to continue even when automation fails. 

This User Task therefore ensures process continuity, human oversight, and operational reliability, as the case can still be assigned appropriately without depending entirely on the automated matching service. 



<img width="1223" height="504" alt="image" src="https://github.com/user-attachments/assets/ab50f2b8-4c57-425c-bce0-e16e2da0fab9" />





### Step 5: Extract Assignments

The task **Extract assignments** retrieves the calculated assignment suggestions from the `assignments` table and sends them back to Camunda.

This step is necessary because the calculated assignments are stored externally in Google Sheets. Camunda therefore needs a service step to fetch the prepared assignment data before a human user can review it.

#### Related Make Scenario: Extract Assignments

<img width="1526" height="438" alt="Make Extract assignments" src="https://github.com/user-attachments/assets/d57e33c6-a02b-4b39-9bc7-bd2aa3e2a394" />


The Make scenario **Extract Assignments** is triggered by a webhook.

The scenario searches the `assignments` table for rows where:

```text
status = OK
```

After finding an assignment row, Make sends the relevant assignment fields back to Camunda through the Camunda `submit-form` endpoint.

The returned variables include for example:

```text
case_id
assignment_id
coach_first_name
coach_last_name
exclusion_reason
language_score
duration_score
skill_score
total_score
coach_skills
case_first_name
case_last_name
case_size_in_procent
case_main_languages
case_other_languages
case_type
distance_text
duration_text
eligible
```

After the data has been returned to Camunda, the assignment row can be marked as processed.

---

### Step 6: Review Assignments

The task **Review assignments** is a user task.

At this stage, the system has already calculated possible coach assignments and gives 2 coaches in the decending order. The coach with the  highest total score is evaluated first in the DMN. The user can now review the suggested coach, the case data, the travel distance, duration, eligibility and scores.

The purpose of this step is not to fully automate the final decision. Instead, the automatic scoring provides decision support. The user can still apply professional judgement before continuing with the final allocation.

Extract Camunda Cockpit
<div style="display: flex; gap: 26px; align-items: flex-start;">
  <img style="height: 620px; width: auto;" alt="image" src="https://github.com/user-attachments/assets/db127198-dfff-4ab6-9b5e-30529eec6c46" />
  
  <img style="height: 620px; width: auto;" alt="image" src="https://github.com/user-attachments/assets/45c9ba14-c790-415c-87e5-4bc6c946a915" />
</div>


### Step 7: Evaluate soft factors 

The task **Evaluate soft factors** is a Business Rule Task. 

At this stage, the system evaluates qualitative suitability criteria that are not fully covered by the previous hard-factor calculation. While the earlier automated step focuses on measurable criteria such as distance, language compatibility, and scoring, this step considers more contextual and qualitative aspects of the coach-case match. The soft factors include case complexity, coach experience, and coach type. 

This task is implemented in Camunda using DMN-based decision logic. The DMN table receives the relevant input values and returns a recommendation outcome indicating whether the proposed Family Coach is suitable for the client case. 

The purpose of this step is to provide structured and transparent decision support for more qualitative criteria. It improves consistency in the evaluation process while still leaving the final judgment to the responsible Case Coach. 

<img width="684" height="350" alt="image" src="https://github.com/user-attachments/assets/f6b4663f-7967-4382-aa5e-880f47ed5ebc" />



<img width="929" height="445" alt="image" src="https://github.com/user-attachments/assets/42838f82-da61-42f7-8c64-6856f65fdfbf" />


### Step 8: Review Family Coach Profile 

The task **Review Family Coach profile** is modeled as a User Task. 

At this stage, the Case Coach reviews the proposed Family Coach in greater detail. This review includes the coach profile, the automated recommendation, and the result of the soft-factor evaluation. 

The Case Coach assesses whether the proposed coach is appropriate for the specific client case. This may include reviewing the coach’s professional experience, employment type, practical suitability for the case, and whether the match is sensible in the real operational context. 

The purpose of this step is to ensure that the final allocation decision is not made solely by the system. Instead, the recommendation is validated by a human expert, which preserves professional judgment and reflects the actual practice of coach allocation in the organisation. 


<u> Configuration Camunda <u>

<img width="268" height="647" alt="Configuration Camunda" src="https://github.com/user-attachments/assets/c0bcfb08-9f92-4df1-8b0a-630ca9ac1c99" />

<u> Extract Camunda Cockpit <u>

<img width="322" height="886" alt="Extract Camunda Cockpit" src="https://github.com/user-attachments/assets/5c1a45fb-3f09-459e-b65e-148715e96721" />


### Step 9: Recommended? 

The element **Recommended?** is an Exclusive Gateway. 

At this point, the process checks whether the Reviewed Family Coach is recommended for the client case. 

If the coach is suitable, the process continues to the next step, where the client is informed about the allocation. 




 <td style="border:1px solid #ccc; padding:8px;">
      <img width="591" height="258" alt="image" src="https://github.com/user-attachments/assets/0f76f170-8d46-432b-a720-889a9330e6bb" />
    </td>





If the coach is not suitable then we inform the client of non-allocation of case. 





<img width="422" height="354" alt="image" src="https://github.com/user-attachments/assets/2646f16d-6322-4cb1-b8bc-16a91e1e4e27" />







The purpose of this gateway is to create a clear decision point in the process. It ensures that only suitable coach recommendations move forward to final communication with the client. 




### Step 10: Notify assignment

The task **Notify Assignment** is a User Task. 

At this stage, the client is informed about the allocation result, depending on the communication channel used by the organisation. 

The Case Coach informs the client that a Family Coach has been selected. 

The purpose of this step is to ensure that the client receives clear confirmation about the allocation before the process ends. 

<img width="430" height="672" alt="image" src="https://github.com/user-attachments/assets/f7cc2943-4cbb-4f66-91cc-eaadd7f965c6" />


### Step 11: Case Assigned 


The event Case assigned is an End Event that marks the completion of the process after the case has been allocated successfully and the client has been informed of the assignment.


### Step 12: Notify Non-assignment

The task **Notify Non-Assignment** is a User Task. 

At this stage, the client is informed about the non-allocation result, depending on the communication channel used by the organisation. 

The Case Coach informs the client that a Family Coach has not been selected. 

The purpose of this step is to ensure that the client receives clear confirmation about the non-allocation before the process ends. 

### Step 13: Case not assigned 



The event Case not assigned is an End Event that marks the completion of the process when no suitable Family Coach could not be allocated and the client has been informed of the non-assignment.




---

## 7. Scoring Logic

The Python scoring script evaluates each possible case-coach combination. The goal of the scoring logic is to identify whether a coach is eligible for a case and, if eligible, how suitable the coach is based on predefined business rules.

The scoring model consists of two parts:

1. **Hard Criteria**  
   These criteria must be fulfilled. If one hard criterion is violated, the coach is not eligible and the total score is set to `0`.

2. **Weighted Score Components**  
   If all hard criteria are fulfilled, the system calculates a score based on language match, travel duration and skill match.


The Python script as well as the Flask API is stores into the Codespace "Fuzzy chainsaw"
Dirctlink to Python Script (Scoring)
[https://fuzzy-chainsaw-q7597pwv9q7434v5g.github.dev/ ](https://github.com/cedricsan13/26SS_Tierpark_Bern/blob/7bd46f0365b2c7f9cbf7b62b6b7333c9cf414bd9/score_assignment.py) 

Dirctlink to Python Script (Flask API)
https://github.com/cedricsan13/26SS_Tierpark_Bern/blob/7bd46f0365b2c7f9cbf7b62b6b7333c9cf414bd9/app.py

<img width="431" height="431" alt="image" src="https://github.com/user-attachments/assets/740fc386-f06d-42af-95b8-a9b6126cf47f" />

---

### 7.1 Hard Criteria

A coach is not eligible if at least one hard criterion is violated.

| No. | Criterion | Rule | Data Type | Description | Consequence |
|---:|---|---|---|---|---|
| H1 | Language Match | `case_main_language != coach_main_language` AND `case_main_language != coach_other_language` AND `case_other_language != coach_main_language` | String comparison | There is no sufficient language overlap between case and coach. | `eligible = false`, `total_score = 0` |
| H2 | Capacity | `coach_remaining_capacity * 1.2 < case_size_in_percent` | Numeric | The coach does not have enough remaining capacity, including a safety factor of 20%. | `eligible = false`, `total_score = 0` |
| H3 | Travel Duration | `duration_value > 10800` | Integer | The travel duration is longer than 3 hours. | `eligible = false`, `total_score = 0` |

If a hard criterion is violated, the scoring result is:

```text
eligible = false
total_score = 0
exclusion_reason = reason for exclusion
```

Example:

```json
{
  "eligible": false,
  "exclusion_reason": "No valid language match",
  "language_score": 0,
  "duration_score": 0,
  "skill_score": 0,
  "total_score": 0
}
```

---

### 7.2 Scoring Model

If all hard criteria are fulfilled, the total score is calculated based on three score components.

| Score Component | Maximum Points | Description |
|---|---:|---|
| Language Score | 30 | Evaluates the language fit between case and coach. |
| Duration Score | 30 | Evaluates the travel duration between coach and client. |
| Skill Score | 40 | Evaluates whether the coach has the required skill for the case type. |
| Total Score | 100 | Sum of all score components. |

The total score is calculated as follows:

```text
total_score = language_score + duration_score + skill_score
```

---

### 7.3 Language Score

The language score evaluates whether the case languages match the coach languages. A main language match receives the highest score. Matches involving secondary languages receive fewer points.

| No. | Rule | Points | Data Type | Meaning |
|---:|---|---:|---|---|
| L1 | `case_main_language = coach_main_language` | 30 | String | Perfect main language match |
| L2 | `case_main_language = coach_other_language` | 15 | String | Case main language matches coach secondary language |
| L3 | `case_other_language = coach_main_language` | 15 | String | Case secondary language matches coach main language |
| L4 | No language match | 0 | String | No language score |

If multiple language rules match, the highest applicable score is used.

Example:

```text
case_main_language = German
coach_main_language = German

language_score = 30
```

---

### 7.4 Duration Score

The duration score evaluates the travel duration between the coach address and the client address. The value `duration_value` is provided by the Google Maps API in seconds.

| No. | Rule | Points | Data Type |
|---:|---|---:|---|
| D1 | `0 < duration_value <= 1800` | 30 | Integer |
| D2 | `1800 < duration_value <= 3600` | 25 | Integer |
| D3 | `3600 < duration_value <= 5400` | 20 | Integer |
| D4 | `5400 < duration_value <= 7200` | 15 | Integer |
| D5 | `7200 < duration_value <= 9000` | 10 | Integer |
| D6 | `9000 < duration_value <= 10800` | 5 | Integer |
| D7 | `duration_value > 10800` | 0 | Integer, but handled as hard criterion |

The shorter the travel duration, the higher the duration score.

Example:

```text
duration_value = 2703

duration_score = 25
```

---

### 7.5 Skill Score

The skill score evaluates whether the case type matches the skills of the coach.

| No. | Rule | Points | Data Type | Meaning |
|---:|---|---:|---|---|
| S1 | `case_type = coach_skills` OR `case_type in coach_skills` | 40 | String | Coach has the required skill for the case |
| S2 | No skill match | 0 | String | Coach does not have the required skill |

The skill comparison supports cases where the coach has multiple skills stored in one field.

Example:

```text
case_type = Kinderbetreuung
coach_skills = Kinderbetreuung, Familienbegleitung

skill_score = 40
```

---

### 7.6 Example Calculation

Example input:

```json
{
  "assignment_id": "CASE-0002-COACH001",
  "case_id": "CASE-0002",
  "coach_id": "COACH001",
  "case_main_language": "German",
  "case_other_language": "French",
  "coach_main_language": "German",
  "coach_other_language": "French",
  "case_type": "Kinderbetreuung",
  "coach_skills": "Kinderbetreuung,Familienbegleitung",
  "case_size_in_percent": 20,
  "coach_remaining_capacity": 80,
  "duration_value": 2703
}
```

Calculation:

```text
Language Score:
case_main_language = coach_main_language
German = German
=> 30 points

Duration Score:
duration_value = 2703
1800 < 2703 <= 3600
=> 25 points

Skill Score:
case_type is included in coach_skills
Kinderbetreuung is included in Kinderbetreuung,Familienbegleitung
=> 40 points

Total Score:
30 + 25 + 40 = 95
```

Example output:

```json
{
  "assignment_id": "CASE-0002-COACH001",
  "case_id": "CASE-0002",
  "coach_id": "COACH001",
  "eligible": true,
  "exclusion_reason": "",
  "language_score": 30,
  "duration_score": 25,
  "skill_score": 40,
  "total_score": 95
}
```

---

### 7.7 Summary of the Scoring Logic

The scoring model ensures that unsuitable coaches are excluded before a score is calculated. This is done through hard criteria for language match, capacity and travel duration.

Only if all hard criteria are fulfilled, the system calculates a weighted score. The total score supports the decision-making process by making coach suitability transparent and comparable.

The final decision is still made by a human user in the review step. The scoring model provides decision support, but it does not fully replace professional judgement.

---

## 8. Make Scenarios

### 8.1 Get Onboarding Data

Purpose:

```text
Read new cases from unassigned_cases and submit them to Camunda.
```

Main modules:

| Module | Purpose |
|---|---|
| Google Sheets Search Rows | Find cases where `camunda_submitted` is empty |
| HTTP Make Request | Submit case variables to Camunda |
| Google Sheets Update Row | Mark case as submitted |

---

### 8.2 Calculate Distances and Score

Purpose:

```text
Create and score all case-coach assignment combinations.
```

Main modules:

| Module | Purpose |
|---|---|
| Webhook | Receive trigger from Camunda |
| Google Sheets Search Rows | Read unassigned cases |
| Google Sheets Update Row | Mark case as assigned or in processing |
| Google Sheets Search Rows | Read coaches |
| Google Maps Distance Matrix | Calculate travel distance and duration |
| Google Sheets Add Row | Create assignment row |
| HTTP Make Request | Call Flask scoring API |
| Google Sheets Update Row | Write score result into assignment row |
| Webhook Response | Return status to Camunda |

---

### 8.3 Extract Assignments

Purpose:

```text
Read calculated assignment suggestions and return them to Camunda.
```

Main modules:

| Module | Purpose |
|---|---|
| Webhook | Receive trigger from Camunda |
| Google Sheets Search Rows | Read assignment rows with `status = OK` |
| HTTP Make Request | Submit assignment variables to Camunda |
| Google Sheets Update Row | Mark assignment row as processed |

---

## 9. Important Mapping Rules

The following mappings are important for the process to work correctly.

### Case Fields from `unassigned_cases`

```text
case_id = {{2.`0`}}
First Name = {{2.`1`}}
Last Name = {{2.`2`}}
Address = {{2.`3`}}
City = {{2.`4`}}
Postal Code = {{2.`5`}}
Main Language = {{2.`6`}}
Other Language = {{2.`7`}}
Urgency = {{2.`8`}}
Type = {{2.`9`}}
Workload = {{2.`10`}}
Case Complexity = {{2.`12`}}
camunda_submitted = {{2.`13`}}
assigned = {{2.`14`}}
```

### Coach Fields from `coaches`

```text
coach_id = {{5.`0`}}
first_name = {{5.`1`}}
last_name = {{5.`2`}}
address = {{5.`3`}}
postal_code = {{5.`4`}}
city = {{5.`5`}}
main_language = {{5.`6`}}
other_language = {{5.`7`}}
skills = {{5.`8`}}
active = {{5.`9`}}
workload = {{5.`10`}}
capacity_max_in_prozent = {{5.`11`}}
remaining_capacity = {{5.`12`}}
coach_experience = {{5.`13`}}
coach_type = {{5.`14`}}
```
2 refers to unassigned_cases spreadsheets

0..14 refers to the columns of the unassigned_cases spreadsheet 

5 refers to coaches spreadsheets

0..14 refers to the columns of the coaches spreadsheet 

---


## 10. Flask API Endpoint

The Flask API exposes the scoring function.

### 10.1 Healthcheck

```http
GET /
```

Expected response:

```json
{
  "status": "ok",
  "message": "Scoring API is running"
}
```

---

### 10.2 Score Assignment

```http
POST /score-assignment
Content-Type: application/json
```

The endpoint receives one assignment candidate and returns the calculated eligibility and scores.

---

## 11. Testing

### 11.1 Test Flask API Locally

Start Flask:

```bash
python app.py
```

Test healthcheck:

```bash
curl http://127.0.0.1:5000/
```

Test scoring endpoint:

```bash
curl -X POST http://127.0.0.1:5000/score-assignment \
  -H "Content-Type: application/json" \
  -d '{
    "assignment_id": "CASE001-COACH001",
    "case_id": "CASE001",
    "coach_id": "COACH001",
    "case_main_language": "German",
    "case_other_language": "French",
    "coach_main_language": "German",
    "coach_other_language": "Italian",
    "case_type": "Kinderbetreuung",
    "coach_skills": "Kinderbetreuung,Familienbegleitung",
    "case_size_in_percent": 30,
    "coach_remaining_capacity": 50,
    "duration_value": 4147
  }'
```

---

### 11.2 Test with Postman

Use the following configuration:

```text
Method: POST
URL: https://<public-flask-url>/score-assignment
Header: Content-Type = application/json
Body: raw JSON
```

---

### 11.3 Test Make Scenario

Recommended test sequence:

1. Test `Get Onboarding Data`.
2. Check that `camunda_submitted = TRUE` is written.
3. Trigger `Calculate Distances and Score`.
4. Check that one assignment row is created per coach.
5. Check that scores are written to `assignments`.
6. Trigger `Extract Assignments`.
7. Check that assignment variables arrive in Camunda.

---

## 12. Resulting Benefits

The TO-BE process provides several improvements compared to the AS-IS process.

| Benefit | Description |
|---|---|
| Less manual effort | Repetitive tasks such as distance checks and scoring are automated. |
| Higher transparency | Assignment decisions are based on visible criteria and scores. |
| Better data quality | Structured forms and database tables reduce inconsistent input. |
| Faster processing | Possible coach assignments are calculated automatically. |
| More objective decision support | Each case-coach combination is evaluated using the same scoring logic. |
| Human control remains | Final review is still performed by a person before the allocation is completed. |

---

## 13. Known Limitations

This implementation is a prototype and uses Google Sheets as a lightweight database. For a production-ready solution, a relational database should be considered.

The Flask API is currently hosted through a development environment. For stable productive usage, the API should be deployed on a permanent hosting service.

The scoring model is rule-based. Future versions could include more sophisticated ranking logic, weighting configuration or manual override rules.

---


## 14. Conclusion

The TO-BE BPMN Camunda model improves the Case allocation process by combining automation with human decision-making. Automated service tasks reduce manual effort by calculating distance, scoring coaches, and extracting assignment suggestions. User tasks ensure that important decisions, such as reviewing assignments and family coach profiles, remain controlled by responsible staff.

The model also includes a clear error handling path, which makes the process more robust when technical problems or missing data occur. The recommendation loop allows the responsible person to reject unsuitable coaches and evaluate alternatives.

Overall, this TO-BE process supports faster, more transparent, and more reliable case allocation. It is suitable for further implementation in Camunda and can be integrated with tools such as Make, Google Sheets, Google Maps, and email services.





# Acknowledgements

We would like to thank the course coaches, Andreas Martin, Charuta Pande, and Devid Montecchiari, as well as the project stakeholders, for their guidance and valuable feedback throughout the Digitalization of Business Processes project. Their expertise and support greatly enhanced this work and played an important role in its successful completion.

