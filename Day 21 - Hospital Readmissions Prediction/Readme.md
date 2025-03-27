# Hospital Readmissions Prediction

## Dataset
- **Source:** [Hospital Readmissions Dataset](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008)
- **Description:** This dataset contains patient records and various medical attributes to predict the likelihood of hospital readmissions.

## Objective
- Develop a classification model to predict if a patient will be readmitted to the hospital.

## 1. Data Preprocessing
- **Missing Values Handling:** Processed missing values appropriately.
- **Feature Encoding:** Applied one-hot encoding and label encoding for categorical variables.
- **Feature Scaling:** Standardized numerical features for better model performance.

## 2. Model Training & Evaluation
- **Algorithms Used:**
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Gradient Boosting
  - XGBoost
  - Neural Network

### Performance Metrics
| Model | Train Accuracy | Test Accuracy | F1 Score (Class 0) | F1 Score (Class 1) | Precision (Class 0) | Precision (Class 1) | Recall (Class 0) | Recall (Class 1) |
|-------|---------------|--------------|------------------|------------------|------------------|------------------|------------------|------------------|
| Logistic Regression | 0.6208 | 0.6160 | 0.6802 | 0.5196 | 0.6082 | 0.6321 | 0.7717 | 0.4411 |
| Decision Tree | 0.9999 | 0.5534 | 0.5802 | 0.5230 | 0.5773 | 0.5260 | 0.5831 | 0.5200 |
| Random Forest | 0.9999 | 0.6228 | 0.6676 | 0.5641 | 0.6256 | 0.6186 | 0.7156 | 0.5185 |
| Gradient Boosting | 0.6378 | 0.6331 | 0.6878 | 0.5550 | 0.6256 | 0.6467 | 0.7638 | 0.4861 |
| XGBoost | 0.6857 | 0.6387 | 0.6812 | 0.5831 | 0.6390 | 0.6383 | 0.7295 | 0.5367 |
| Neural Network | 0.6322 | 0.6203 | 0.6876 | 0.5158 | 0.6089 | 0.6451 | 0.7898 | 0.4297 |

## 3. Key Observations
- Decision Tree & Random Forest models overfit the training data.
- Gradient Boosting and XGBoost provided the best balance between performance and generalization.
- Logistic Regression had moderate accuracy but performed well in interpretability.
- Neural Network performed decently but required hyperparameter tuning.

## 4. Next Steps
- Improve hyperparameter tuning for boosting models.
- Try feature engineering to extract more insights.
- Address class imbalance to improve recall.

## 5. Tools Used
- **Python Libraries:** Pandas, NumPy, Scikit-learn, XGBoost, TensorFlow/Keras

### Summary:
This project involved building predictive models to determine hospital readmissions. Gradient Boosting and XGBoost performed the best in terms of accuracy and balance between precision-recall. Future improvements could include advanced feature engineering and hyperparameter tuning.

