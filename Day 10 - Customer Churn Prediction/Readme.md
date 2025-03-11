# Churn Prediction Project

## 📚 Project Scope
The primary objective of this project is to build machine learning models that can accurately predict customer churn for a telecom company. Customer churn refers to the rate at which customers stop doing business with a company. By predicting churn, businesses can implement strategies to retain customers and reduce loss.

## 📊 Dataset Description
- **Source:** [Kaggle - Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- **Features:**
  - **CustomerID:** Unique ID for each customer.
  - **Demographics:** Gender, SeniorCitizen, Partner, Dependents.
  - **Service Details:** PhoneService, MultipleLines, InternetService, etc.
  - **Account Information:** Contract type, Payment method, Monthly and Total Charges.
  - **Target Variable:** `Churn` (Yes/No)

## ⚙️ Preprocessing Steps
1. **Handling Missing Values:**
   - Missing or erroneous data points were identified and handled appropriately.
2. **Encoding Categorical Variables:**
   - Label Encoding and One-Hot Encoding were used to convert categorical variables into numerical formats.
3. **Feature Scaling:**
   - StandardScaler was used to normalize numerical features.
4. **Train-Test Split:**
   - The dataset was split into 80% training and 20% testing sets.

## 📈 Observations from Visualizations
- Customers with month-to-month contracts exhibited higher churn rates.
- Customers without partners and dependents were more likely to churn.
- Higher monthly charges correlated with higher churn probability.
- Senior citizens had a slightly higher churn rate compared to younger customers.

## 🧠 Models Used and Performance
The following models were trained and evaluated on the test data. Metrics like F1 Score, Precision, and Recall were calculated for both Class 0 (No Churn) and Class 1 (Churn):

| Model                         | Class 0 F1 | Class 0 Precision | Class 0 Recall | Class 1 F1 | Class 1 Precision | Class 1 Recall |
|------------------------------|------------|-------------------|----------------|------------|-------------------|----------------|
| **Linear Regression**         | 0.86       | 0.86              | 0.87           | 0.59       | 0.59              | 0.58           |
| **Logistic Regression**       | 0.87       | 0.85              | 0.89           | 0.58       | 0.63              | 0.54           |
| **Decision Tree**             | 0.82       | 0.83              | 0.81           | 0.47       | 0.46              | 0.49           |
| **Random Forest**             | 0.86       | 0.83              | 0.89           | 0.52       | 0.60              | 0.47           |
| **Multi-Layer Perceptron**    | 0.86       | 0.86              | 0.87           | 0.58       | 0.60              | 0.56           |
| **Gradient Boosting Classifier** | 0.87    | 0.85              | 0.90           | 0.58       | 0.64              | 0.53           |

## 🏆 Best Performing Model
The **Gradient Boosting Classifier** performed the best overall:
- Achieved the highest recall and precision scores for Class 1 (Churn).
- Balanced performance across both classes, indicating better generalization.
- Gradient Boosting's ensemble approach helped in capturing complex patterns and reducing overfitting.

## 🛠️ Resources Used
- Python Libraries: `Pandas`, `NumPy`, `Matplotlib`, `Seaborn`, `Scikit-learn`
- Dataset: [Kaggle - Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

---
This project demonstrates a systematic approach to predicting customer churn using multiple machine learning models, ultimately selecting the one with the best performance metrics. 🚀

