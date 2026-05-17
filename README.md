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



# Description of the Use Case



# Current Situation



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


# Conclusion

The TO-BE BPMN Camunda model improves the Case allocation process by combining automation with human decision-making. Automated service tasks reduce manual effort by calculating distance, scoring coaches, and extracting assignment suggestions. User tasks ensure that important decisions, such as reviewing assignments and family coach profiles, remain controlled by responsible staff.

The model also includes a clear error handling path, which makes the process more robust when technical problems or missing data occur. The recommendation loop allows the responsible person to reject unsuitable coaches and evaluate alternatives.

Overall, this TO-BE process supports faster, more transparent, and more reliable case allocation. It is suitable for further implementation in Camunda and can be integrated with tools such as Make, Google Sheets, Google Maps, and email services.

# Acknowledgements

We would like to thank the course coaches, Andreas Martin, Charuta Pande and Devid Montecchiari and project stakeholders for their guidance and feedback during the Digitalization of Business Processes project.Their expertise and dedication have been the driving force behind our success, and we are deeply thankful for their invaluable contributions.
