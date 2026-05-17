# TO-BE BPMN Camunda Model: Case Allocation Process

![BPMN Model Screenshot](add-your-camunda-model-screenshot-here)

# Team Members

| Name | Email |
|------|-------|
| Cedric Iseli | cedric.iseli@students.fhnw.ch|
| Dionis Mrlaku| dionis.mrlaku@students.fhnw.ch|
| Kanika Mukhija|kanika.mukhija@students.fhnw.ch |
| Pallavi Gowda| pallavi.gowda@students.fhnw.ch |
| Shakunthala Reddy Patlolla|shakunthalareddy.patlolla@students.fhnw.ch  |

# Team Coach

1. Charuta Pande
2. Andreas Martin
2. Devid Montecchiari

# Introduction

This document describes the TO-BE BPMN model for the Case allocation process. The model was created as part of the Digitalization of Business Processes project and is designed for implementation in Camunda.

The purpose of the TO-BE model is to digitalize and standardize the way incoming client cases are captured, checked, evaluated, and assigned to a suitable family coach. The process supports automated pre-selection of coaches based on distance and scoring, while still keeping human review steps for final decision-making and quality control.

# Description of the Use Case

The use case focuses on the allocation of a new client case to an appropriate family coach. In the current manual way of working, the case coach or responsible person needs to collect client information, compare coach availability, consider distance, evaluate personal or soft factors, and finally inform the client after a suitable coach has been selected.

The TO-BE process improves this by using Camunda as the process orchestration platform. Client data is entered through a form, automated service tasks calculate distance and scoring, assignments are extracted from the system, and user tasks allow the responsible person to review the recommended coach before the client is informed.

The goal of this process is to ensure that each case is assigned in a structured, transparent, and timely way. The model also includes error handling for situations where automatic distance calculation or scoring fails.

# Current Situation

In the manual AS-IS situation, case allocation depends heavily on individual coordination and manual checking.

* Client information is collected manually.
* The responsible person checks available family coaches manually.
* Distance and suitability are not automatically calculated.
* Soft factors, such as language, experience, specialization, and client needs, may be evaluated informally.
* If the first coach is not suitable, the responsible person needs to search again manually.
* There is no clear automated error handling when data is missing or system checks fail.
* The client is informed only after the internal assignment decision has been completed.

Because of these manual steps, the process can become slow, inconsistent, and difficult to monitor. This is especially problematic when the case should be assigned or delayed within a limited time frame.

# AS-IS Pain Points

1. **Manual case handling**  
   The responsible person must manually collect and compare all information needed for the assignment.

2. **Time-consuming coach selection**  
   Finding a suitable family coach can take time, especially if several coaches need to be checked.

3. **Limited transparency**  
   It is difficult to clearly track why a specific coach was selected or rejected.

4. **No automated distance calculation**  
   Distance or travel time between the client and possible family coaches is not automatically calculated.

5. **No structured scoring**  
   Suitability decisions may depend on personal judgment without a standard scoring logic.

6. **Weak error handling**  
   If information is missing or automatic checks fail, the process needs a clear exception path.

7. **Client communication delay**  
   The client is informed only after the internal decision is completed, which can lead to delays if responsibilities are unclear.

# TO-BE Process

## Process Overview

The TO-BE process is modeled as one main Camunda BPMN process called **CaseAllocation66**. The process starts when a new client case is created and ends when the case has been assigned and the client has been informed.

The process contains the following main stages:

1. **Client data entry**  
   The responsible user enters the client data through a form.

2. **Automated distance and score calculation**  
   The system calculates distance and scoring values for potential family coaches.

3. **Assignment extraction**  
   The system extracts possible assignments based on the calculated results.

4. **Assignment review**  
   A responsible user reviews the proposed assignments.

5. **Soft factor evaluation**  
   A business rule task evaluates qualitative criteria such as suitability, preferences, or case-specific factors.

6. **Family coach profile review**  
   The responsible user reviews the selected family coach profile.

7. **Recommendation decision**  
   An exclusive gateway checks whether the family coach is recommended.

8. **Client notification**  
   If the coach is recommended, the client is informed.

9. **Case assigned**  
   The process ends after the client has been informed and the case is assigned.

If a technical error occurs during distance and score calculation, the process uses a boundary error event and moves to an error review task.

# Description of the TO-BE Process Elements

| Row | BPMN Element | Element Name | Description | Comment |
|-----|-------------|--------------|-------------|---------|
| 1 | Start Event | Start | The process starts when a new client case needs to be allocated. | This represents the beginning of the case allocation workflow. |
| 2 | User Task | Enter client data (Forms) | The responsible person enters client details into a digital form. | This replaces manual collection of client data and ensures structured input. |
| 3 | Service Task | Calculate Distances and Score | The system calculates distance and scoring for possible family coaches. | This supports objective pre-selection of suitable coaches. |
| 4 | Boundary Error Event | Error on distance/score calculation | Captures technical or data-related errors during the calculation step. | If the service task fails, the process moves to error handling. |
| 5 | User Task | Review error | The responsible person reviews the error and decides how to correct it. | This ensures that failed automated checks do not stop the complete process without action. |
| 6 | Manual Task | Assign manually | The responsible person manually assigns or prepares the case when automation fails. | This is a fallback path for exceptional cases. |
| 7 | Service Task | Extract assignments | The system extracts possible coach assignments from the calculated results. | This prepares the candidate list for human review. |
| 8 | User Task | Review assignments | The responsible person reviews the proposed coach assignments. | This keeps human control in the process before final recommendation. |
| 9 | Business Rule Task | Evaluate soft factors | The system evaluates qualitative rules for suitability. | This can be implemented using DMN decision logic in Camunda. |
| 10 | User Task | Review Family Coach profile | The responsible person checks the selected family coach profile. | Ensures that the coach is suitable for the specific case. |
| 11 | Exclusive Gateway | Recommended? | Decision point to check whether the family coach is recommended. | If yes, the process continues to client notification. If no, the process loops back to evaluate another option. |
| 12 | User Task | Inform client | The client is informed about the selected family coach or assignment outcome. | This is the final communication step before process completion. |
| 13 | End Event | Case assigned | The process ends after the case has been successfully assigned. | Marks successful completion of the TO-BE process. |

# Process 1: Client Data Entry and Automated Pre-Selection

![Client Data Entry and Automated Pre-Selection](add-screenshot-here)

## Step 1: Enter Client Data

The process begins with the user task **Enter client data (Forms)**. In this step, the responsible person enters the required client information into a structured form.

Typical form data can include:

* Client name or case ID
* Address or location
* Required support type
* Language needs
* Urgency or priority
* Special requirements
* Preferred family coach criteria

This step is important because the later automated calculation depends on complete and correct input data.

## Step 2: Calculate Distances and Score

After the client data is submitted, the service task **Calculate Distances and Score** is executed. This task is responsible for checking possible family coaches and calculating values that support the allocation decision.

The calculation can include:

* Distance between client and coach
* Estimated travel time
* Coach availability
* Matching score based on criteria
* Priority or ranking of possible coaches

This task can be connected to external tools such as Make, Google Sheets, or a mapping service. In Camunda, this service task should be implemented using a connector, external task worker, or API call.

## Step 3: Handle Calculation Errors

A boundary error event is attached to the **Calculate Distances and Score** service task. If the service task fails, for example because of missing address data, API failure, or invalid input, the process does not continue directly to assignment extraction.

Instead, the process moves to **Review error**. The responsible user checks the issue and then continues with **Assign manually**. This ensures that exceptional cases can still be handled without losing the case.

# Process 2: Assignment Review and Soft Factor Evaluation

![Assignment Review and Soft Factor Evaluation](add-screenshot-here)

## Step 1: Extract Assignments

If the distance and score calculation is successful, the service task **Extract assignments** is executed. This task prepares the list of possible family coach assignments.

The output can include:

* Best matching coach
* Alternative coach options
* Distance and score values
* Availability status
* Reason for recommendation

This supports the responsible person by providing a ranked and structured overview instead of requiring a fully manual search.

## Step 2: Review Assignments

The user task **Review assignments** allows the responsible person to check the system-generated assignment suggestions.

The user can verify:

* Whether the suggested coach is available
* Whether the assignment fits the client need
* Whether the score and distance are acceptable
* Whether an alternative coach should be considered

This step is important because the final decision should not be based only on automatic scoring.

## Step 3: Evaluate Soft Factors

The business rule task **Evaluate soft factors** evaluates additional qualitative criteria. In Camunda, this step can be implemented with a DMN decision table.

Possible soft factors include:

* Language match
* Gender preference, if relevant and allowed by the process rules
* Experience with similar cases
* Specialization of the family coach
* Current workload
* Urgency of the case
* Client-specific needs

The output of this task helps determine whether the suggested family coach should be recommended.

# Process 3: Family Coach Review and Recommendation Decision

![Family Coach Review and Recommendation Decision](add-screenshot-here)

## Step 1: Review Family Coach Profile

The user task **Review Family Coach profile** allows the responsible person to check the selected family coach in detail.

The review can include:

* Coach name and contact details
* Current availability
* Distance from client
* Workload
* Skills and experience
* Suitability for the case

This step provides the final human validation before the client is informed.

## Step 2: Recommended?

The exclusive gateway **Recommended?** checks whether the selected coach is suitable.

There are two possible paths:

### Yes path

If the coach is recommended, the process continues to **Inform client**.

### No path

If the coach is not recommended, the process loops back to **Evaluate soft factors**. This allows the process to review another option or re-evaluate the assignment logic before a final decision is made.

This loop is useful because the first suggested coach may not always be the best choice.

# Process 4: Inform Client and Complete Case Assignment

![Inform Client and Complete Case Assignment](add-screenshot-here)

## Step 1: Inform Client

After a family coach has been recommended, the user task **Inform client** is completed. The client is informed about the assignment decision.

The communication can include:

* Name of the assigned family coach
* Expected next steps
* Contact or appointment information
* Confirmation that the case has been accepted and assigned

In the future, this task could also be automated through Make, Gmail, or another email integration. However, keeping it as a user task is also acceptable if the communication should be checked manually before sending.

## Step 2: Case Assigned

The process ends with the end event **case assigned**. This confirms that the case has been successfully allocated and the client has been informed.

# Error Handling

The model includes an error handling path attached to the service task **Calculate Distances and Score**.

## Error Scenario

An error can occur when:

* The client address is missing or invalid.
* The coach address is missing or invalid.
* The external distance calculation service fails.
* The scoring logic cannot be executed.
* Required variables are missing in Camunda.
* The Make scenario or API response is not received correctly.

## Error Flow

When an error occurs:

1. The boundary error event catches the error.
2. The process moves to **Review error**.
3. The responsible user checks the problem.
4. The case is moved to **Assign manually**.
5. The process continues to **Evaluate soft factors**.

This design is useful because it prevents the process from getting stuck at the automated service task.

# Camunda Implementation Notes

## Forms

The task **Enter client data (Forms)** should use a Camunda form. The form should collect all required variables for the later service tasks and decision logic.

Recommended variables:

| Variable Name | Example Type | Purpose |
|--------------|--------------|---------|
| clientName | String | Name of the client |
| clientAddress | String | Address used for distance calculation |
| casePriority | String | Priority of the case |
| requiredLanguage | String | Language requirement |
| supportType | String | Type of support needed |
| preferredCoachGender | String | Optional matching criterion |
| caseNotes | String | Additional comments |

## Service Task: Calculate Distances and Score

This task should call an external service or Make scenario. The service should return calculated values to Camunda.

Recommended output variables:

| Variable Name | Example Type | Purpose |
|--------------|--------------|---------|
| distanceKm | Number | Distance between client and coach |
| travelTimeMinutes | Number | Estimated travel time |
| coachScore | Number | Suitability score |
| recommendedCoachId | String | ID of suggested coach |
| calculationStatus | String | Success or error status |

## Service Task: Extract Assignments

This task should extract the best coach options from the calculation results.

Recommended output variables:

| Variable Name | Example Type | Purpose |
|--------------|--------------|---------|
| assignmentList | JSON / Object | List of possible coaches |
| firstChoiceCoach | String | Best matching coach |
| alternativeCoach | String | Backup option |
| assignmentStatus | String | Status of assignment extraction |

## Business Rule Task: Evaluate Soft Factors

This task should use a DMN table to evaluate whether the coach is suitable. The decision table can compare the client needs with coach attributes.

Possible DMN inputs:

* requiredLanguage
* coachLanguage
* supportType
* coachSpecialization
* travelTimeMinutes
* coachAvailability
* casePriority
* currentWorkload

Possible DMN outputs:

* recommended = true / false
* recommendationReason
* nextAction

## Exclusive Gateway: Recommended?

The gateway should use the result from the business rule task.

Recommended conditions:

* Yes path: `recommended = true`
* No path: `recommended = false`

The no path loops back to the soft factor evaluation so that another coach can be considered.

# Suggested Improvements

1. **Add a timer boundary event for 24-hour response time**  
   If the family coach does not respond within 24 hours, a timer boundary event can trigger an alternative coach selection path.

2. **Add an availability confirmation task**  
   Before informing the client, the selected family coach could confirm availability.

3. **Add alternative coach logic**  
   The process can automatically select the next best coach if the first coach is unavailable.

4. **Automate client notification**  
   The **Inform client** task can be changed from a user task to a service task if the email should be sent automatically.

5. **Store assignment history**  
   A service task can update Google Sheets or another database with the final assignment decision.

6. **Add clearer escalation handling**  
   If no coach is suitable, the process can escalate to the case coach or leadership.

7. **Improve auditability**  
   Store the reason for recommendation or rejection as process variables.

# Conclusion

The TO-BE BPMN Camunda model improves the internal case review and family coach allocation process by combining automation with human decision-making. Automated service tasks reduce manual effort by calculating distance, scoring coaches, and extracting assignment suggestions. User tasks ensure that important decisions, such as reviewing assignments and family coach profiles, remain controlled by responsible staff.

The model also includes a clear error handling path, which makes the process more robust when technical problems or missing data occur. The recommendation loop allows the responsible person to reject unsuitable coaches and evaluate alternatives.

Overall, this TO-BE process supports faster, more transparent, and more reliable case allocation. It is suitable for further implementation in Camunda and can be integrated with tools such as Make, Google Sheets, Google Maps, and email services.

# Acknowledgements

We would like to thank the course coaches and project stakeholders for their guidance and feedback during the Digitalization of Business Processes project.
