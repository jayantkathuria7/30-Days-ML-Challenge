# Loan Approval Prediction

## Dataset
- **Source:** [Kaggle - Loan Prediction Dataset](https://www.kaggle.com/datasets/leonbora/analytics-vidhya-loan-prediction/data)
- **Description:** This dataset contains loan applicant details, including demographics, credit history, loan amount, and other financial indicators to predict loan approval status.

## Model Performance
| Model                | Train Accuracy | Test Accuracy | F1 Score - Class 0 | F1 Score - Class 1 |
|----------------------|---------------|--------------|-------------------|-------------------|
| Logistic Regression | 0.8065        | 0.8374       | 0.6000            | 0.8979            |
| Decision Tree       | 1.0000        | 0.6585       | 0.4474            | 0.7529            |
| Random Forest      | 1.0000        | 0.7724       | 0.5000            | 0.8526            |
| Gradient Boosting  | 0.8859        | 0.7886       | 0.5357            | 0.8632            |
| SVM                | 0.8167        | 0.8293       | 0.5714            | 0.8934            |
| XGBoost            | 1.0000        | 0.8293       | 0.6769            | 0.8840            |

## Constraints & Challenges
- **Small Dataset:** The limited number of samples affects the generalizability and stability of complex models.
- **Overfitting:** Some models (e.g., Decision Tree, Random Forest, XGBoost) achieved 100% accuracy on the training set but performed worse on the test set, indicating overfitting.
- **Imbalanced Classes:** Class 1 (approved loans) had a higher occurrence, making class 0 (rejected loans) harder to predict accurately.

## 1. Data Preprocessing
- **Missing Values:** Handled missing values using mean/mode imputation where necessary.
- **Categorical Encoding:** One-hot encoding applied to categorical variables.
- **Feature Scaling:** Standardization applied to numerical columns to improve model performance.

## 2. Exploratory Data Analysis (EDA)
- **Loan Approval Rate:** A higher number of approved loans compared to rejected ones.
- **Impact of Credit History:** Applicants with a credit history had a significantly higher chance of loan approval.
- **Income vs. Loan Amount:** Higher incomes were correlated with larger loan amounts but did not always guarantee approval.
- **Gender & Loan Approval:** Slight variance in approval rates between male and female applicants.

## 3. Model Selection & Evaluation
- **Best Model:** Logistic Regression achieved a good balance with **83.7% test accuracy** and an **F1 score of 0.8979** for approved loans.
- **Trade-offs:**
  - Decision Tree and Random Forest had perfect training accuracy but lower test accuracy due to overfitting.
  - Gradient Boosting performed well, achieving a good balance between precision and recall.
  - SVM performed competitively but was computationally expensive.
  - XGBoost showed strong performance but still overfitted slightly.

## 4. Key Insights
- **Credit History is Crucial:** The most influential feature for predicting loan approval.
- **Income Alone is Not Enough:** Applicants with higher incomes were not always approved, showing that other factors (e.g., credit history, loan amount) play a role.
- **Simpler Models Work Well:** Logistic Regression performed well despite being a basic model, proving that complex models aren't always necessary for small datasets.

## 5. Conclusion & Recommendations
- **Handling Overfitting:** Regularization techniques and pruning can improve Decision Trees and Random Forest performance.
- **Data Augmentation:** Increasing dataset size through synthetic data generation could improve model stability.
- **Further Experiments:** Trying ensemble methods or stacking models to improve predictions.

## 6. Tools Used
- **Python Libraries:** Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn

### Key Takeaway:
Credit history is the dominant factor in loan approval, and simpler models like Logistic Regression can be highly effective for small datasets.

