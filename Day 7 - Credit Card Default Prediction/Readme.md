# Credit Card Default Prediction

## Project Description
Credit card default prediction is crucial for financial institutions to mitigate risks associated with lending. This project leverages machine learning techniques to analyze customer financial behavior and predict default probability based on past transactions, credit history, and demographic factors. By identifying high-risk customers, banks can make informed decisions regarding credit approvals, limit adjustments, and risk management strategies.

## Dataset
The dataset contains information about credit card clients, including their credit limit, payment history, bill amounts, and demographic details.

- The dataset is available on **GitHub** (Jupyter Notebook & dataset included)
- Can also be accessed from Kaggle: [Default of Credit Card Clients Dataset](https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset)

### Features Used:
- **LIMIT_BAL**: Credit Limit
- **AGE**: Age of the cardholder
- **BILL_AMT1 - BILL_AMT6**: Bill statements for the last 6 months
- **PAY_0 - PAY_6**: Past payment history
- **PAY_AMT1 - PAY_AMT6**: Amount paid in the last 6 months
- **EDUCATION, MARRIAGE, SEX**: Demographic features

## Data Preprocessing
- Handled missing values
- Performed feature scaling using **StandardScaler**
- Encoded categorical variables
- Split the dataset into **training (80%)** and **testing (20%)** sets

## Models Used & Performance

| Model | Accuracy | Precision (Class 0) | Recall (Class 0) | F1-Score (Class 0) | Precision (Class 1) | Recall (Class 1) | F1-Score (Class 1) |
|--------|----------|------------------|----------------|----------------|------------------|----------------|----------------|
| **BernoulliNB** | 66.53% | 82% | 73% | 77% | 32% | 43% | 36% |
| **Logistic Regression (Balanced)** | 67.85% | 88% | 68% | 77% | 37% | 66% | 48% |
| **Decision Tree** | 71.98% | 82% | 81% | 82% | 38% | 40% | 39% |
| **Random Forest** | 81.63% | 84% | 94% | 89% | 66% | 37% | 47% |
| **XGBoost** | 81.07% | 84% | 94% | 89% | 63% | 35% | 45% |
| **Decision Tree Regressor** | 72.00% | 82% | 81% | 81% | 37% | 40% | 39% |
| **MLP Classifier** | 81.07% | 84% | 94% | 88% | 63% | 37% | 47% |
| **K-Nearest Neighbors** | 79.07% | 83% | 92% | 87% | 55% | 34% | 42% |

## Insights
- **Random Forest** and **XGBoost** performed the best in terms of accuracy.
- **Logistic Regression (Balanced)** improved recall for defaulters but had lower precision.
- **KNN & MLPClassifier** performed well but were slower due to high computational complexity.

## Challenges Faced
- **Class Imbalance**: The dataset had significantly fewer defaulters, requiring techniques like **class weighting** to improve recall.
- **Feature Engineering**: Selecting the most relevant features was challenging and required iterative testing.
- **Hyperparameter Tuning**: Some models like **XGBoost** and **MLPClassifier** needed extensive tuning for better performance.
- **Training Time**: Computational complexity was an issue for models like **KNN** and **MLPClassifier**, making them slower than others.

## Future Improvements
- Tune hyperparameters for **XGBoost** and **Random Forest**
- Try ensemble methods like **Stacking & Boosting**
- Explore deep learning models like **LSTMs** for time-series features
- Perform feature selection to remove redundant variables

---
