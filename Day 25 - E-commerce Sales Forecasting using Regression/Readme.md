# E-Commerce Sales Forecasting Using Regression

## 📊 Project Overview
This project aims to predict **E-Commerce Sales** using various **Regression Models**. The dataset consists of multiple features that influence sales, and different models were evaluated to determine the best-performing one.

- **Kaggle Notebook:** [View Here](https://www.kaggle.com/code/jayantkathuria/e-commerce-sales-forecasting-using-regression)
- **Dataset Used:** [E-Commerce Sales Prediction Dataset](https://www.kaggle.com/datasets/nevildhinoja/e-commerce-sales-prediction-dataset)

---

## 📂 Dataset Information
- **Source:** Kaggle
- **Number of Features:** 7
- **Target Variable:** Sales
- **Key Attributes:**
  - Date
  - Product Category
  - Price
  - Discount
  - Advertising Expenditure
  - Competitor Pricing
  - Demand Factor
  
---

## 🔄 Data Preprocessing Steps
✔ Removed missing values
✔ Converted Date column to datetime format
✔ Feature encoding for categorical variables
✔ Feature scaling using StandardScaler
✔ Splitting dataset into **train (80%)** and **test (20%)**

---

## 🔢 Regression Models Used
### **Models Implemented:**
- **Linear Regression**
- **Decision Tree Regression**
- **Random Forest Regression**
- **Gradient Boosting Regression**
- **XGBoost Regression**
- **Support Vector Regression (SVR)**

### **Performance Comparison** (R-Squared Scores)
| Model | Train R² Score | Test R² Score |
|--------|---------------|--------------|
| Linear Regression | 0.76 | 0.74 |
| Decision Tree | 0.99 | 0.63 |
| Random Forest | 0.98 | 0.79 |
| Gradient Boosting | 0.88 | 0.81 |
| XGBoost | 0.91 | 0.83 |
| SVR | 0.67 | 0.65 |

---

## 📊 Key Findings
- **Linear Regression & SVR** performed poorly on test data.
- **Decision Trees overfitted** (high training score, low test score).
- **Gradient Boosting & XGBoost showed the best generalization.**
- **Feature Engineering & Hyperparameter Tuning** could further improve results.

---

## ⚙️ How to Run the Project
1. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn xgboost
   ```
2. Run the Jupyter Notebook step-by-step.
3. Analyze the performance of different models.

---

## 🛠️ Tools & Libraries Used
- **Python**
- **Pandas, NumPy** - Data Handling
- **Matplotlib, Seaborn** - Data Visualization
- **Scikit-learn, XGBoost** - Machine Learning Models

---

🚀 **This project demonstrates the use of multiple regression models to predict e-commerce sales. Future improvements include advanced feature selection and deep learning models for better accuracy.**
