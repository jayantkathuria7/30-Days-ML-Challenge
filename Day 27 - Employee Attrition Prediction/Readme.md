# Employee Attrition Prediction

## Project Overview
This project analyzes employee attrition using machine learning models. The dataset comes from IBM HR Analytics and contains various employee attributes such as Age, Department, BusinessTravel, and JobRole. The goal is to predict whether an employee will leave the company based on these features.

## Dataset
- **Source:** [IBM HR Analytics Attrition Dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- **Features:** 35 columns, including categorical and numerical variables
- **Target Variable:** `Attrition` (Yes/No)

## Exploratory Data Analysis (EDA)
1. **Data Inspection:**
   - Checked for missing values and duplicates (None found).
   - Separated categorical and numerical features.
   - Identified class imbalance (83.88% stayed, 16.12% left).
2. **Visualizations:**
   - Pie chart of attrition distribution.
   - Feature distributions and correlations.

## Preprocessing
- **Label Encoding**: Converted categorical variables to numerical format.
- **Train-Test Split**: Split the data into training and testing sets.
- **Class Imbalance Handling**: Applied **SMOTE (Synthetic Minority Over-sampling Technique)** to improve model performance for the minority class.

## Models & Performance Comparison

| Model | Train Accuracy | Test Accuracy | F1 Score (Class 0) | F1 Score (Class 1) | Precision (Class 0) | Precision (Class 1) | Recall (Class 0) | Recall (Class 1) |
|--------|----------------|--------------|----------------|----------------|----------------|----------------|---------------|---------------|
| Logistic Regression | 0.872 | 0.881 | 0.933 | 0.493 | 0.883 | 0.850 | 0.988 | 0.347 |
| Decision Tree | 1.000 | 0.752 | 0.848 | 0.330 | 0.868 | 0.300 | 0.829 | 0.367 |
| Random Forest | 1.000 | 0.850 | 0.917 | 0.241 | 0.853 | 0.778 | 0.992 | 0.143 |
| Gradient Boosting | 0.957 | 0.861 | 0.921 | 0.406 | 0.872 | 0.700 | 0.976 | 0.286 |
| XGBoost | 1.000 | 0.854 | 0.917 | 0.377 | 0.869 | 0.650 | 0.971 | 0.265 |

### Performance After Applying SMOTE

| Model | Train Accuracy (SMOTE) | Test Accuracy (SMOTE) | F1 Score (Class 0) | F1 Score (Class 1) | Precision (Class 0) | Precision (Class 1) | Recall (Class 0) | Recall (Class 1) |
|--------|----------------|--------------|----------------|----------------|----------------|----------------|---------------|---------------|
| Logistic Regression | 0.756 | 0.757 | 0.731 | 0.779 | 0.758 | 0.756 | 0.706 | 0.802 |
| Decision Tree | 1.000 | 0.844 | 0.838 | 0.850 | 0.816 | 0.872 | 0.861 | 0.829 |
| Random Forest | 1.000 | 0.943 | 0.941 | 0.946 | 0.918 | 0.968 | 0.965 | 0.924 |
| Gradient Boosting | 0.967 | 0.901 | 0.899 | 0.903 | 0.858 | 0.946 | 0.944 | 0.863 |
| XGBoost | 1.000 | 0.911 | 0.908 | 0.914 | 0.882 | 0.940 | 0.935 | 0.890 |

**Key Observations:**
- SMOTE significantly improved performance for the minority class (Attrition = Yes).
- The F1-score and recall for Class 1 (Attrition = Yes) increased across all models.
- XGBoost and Random Forest performed the best after SMOTE.

## Notebook Link
You can explore the complete notebook here: [Kaggle Notebook](https://www.kaggle.com/code/jayantkathuria/employee-attrition/notebook)

## How to Run
1. Install dependencies: `pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn`
2. Load the dataset.
3. Run the Jupyter Notebook.

## Future Improvements
- Feature engineering to add more meaningful features.
- Hyperparameter tuning to improve model performance.
- Deploying the model using Flask or FastAPI.

---

This project provides insights into employee attrition and demonstrates the impact of handling class imbalance with SMOTE. 🚀

