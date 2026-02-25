# Dataset: Diabetes 130-US hospitals (1999-2008)

This dataset represents 10 years of clinical care across 130 hospitals in the United States. It is ideal for multiclass or binary classification tasks focused on **hospital readmission**.

## General Information
- **Original Source:** [UCI Machine Learning Repository - ID 296](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008)
- **Instances:** 101,766
- **Features:** 47 (a mix of categorical, integer, and string variables)
- **Target Variable (`readmitted`):** - `<30`: Readmitted in less than 30 days (High risk).
    - `>30`: Readmitted in more than 30 days.
    - `No`: No record of readmission.

## File Descriptions
- `diabetic_data.csv`: The primary dataset. It contains 101,766 hospital admission records with 50 attributes (columns), including demographics, laboratory scores, diagnoses, and medications. The final column (`readmitted`) serves as the target variable.
- `IDS_mapping.csv`: The "code dictionary." This file is crucial for interpretability, as it maps the numerical IDs from three key columns (`admission_type_id`, `discharge_disposition_id`, and `admission_source_id`) to their textual descriptions. For example, it allows you to identify whether a patient was discharged home or to a hospice facility.
