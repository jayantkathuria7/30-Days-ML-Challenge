# 🔧 Predictive Maintenance using Sensor Data

## 📌 Project Overview
This project focuses on predicting **machine failures** using sensor data. By analyzing historical sensor readings, machine learning models are trained to classify:
1. **Whether a failure will occur** (Binary Classification)
2. **The type of failure** (Multi-Class Classification)

This enables **proactive maintenance**, reducing downtime and improving efficiency.

---

## 📂 Dataset Information

🔗 **Project Notebook on Kaggle:** [Click Here](https://www.kaggle.com/code/jayantkathuria/predictive-maintenance-using-sensor-data)
- **Source:** [Kaggle - Predictive Maintenance Dataset](https://www.kaggle.com/code/jayantkathuria/predictive-maintenance-using-sensor-data)
- **Size:** 10,000 rows × 14 features
- **Key Features:**
  - **Air Temperature [K]**, **Process Temperature [K]**, **Rotational Speed [rpm]**, **Torque [Nm]**, **Tool Wear [min]**
  - **Target 1:** **Failure or Not** (Binary Classification)
  - **Target 2:** **Type of Failure** (Multi-Class Classification)
- **Preprocessing:**
  - Dropped **UID** and **Product ID** (not needed for prediction)
  - Renamed columns for better readability
  - Removed ambiguous rows

---

## 🔄 Project Workflow

### 📌 1. Data Preprocessing
✔️ Checked for missing and duplicate values (**None found**)
✔️ Encoded categorical columns
✔️ Scaled numerical features for better model performance
✔️ Addressed **class imbalance** using **SMOTE**

### 📌 2. Exploratory Data Analysis (EDA)
✔️ **Histograms** to visualize feature distributions (hue: target values)
✔️ **Pie charts & value counts** for categorical features
✔️ **Correlation heatmap** to understand feature relationships

### 📌 3. Machine Learning Models
**Task 1: Predicting Machine Failure (Binary Classification)**
✔️ Applied multiple ML models
✔️ Balanced dataset using **SMOTE**
✔️ Evaluated model performance

**Task 2: Predicting Failure Type (Multi-Class Classification)**
✔️ Repeated classification process
✔️ Applied **SMOTE** to handle class imbalance
✔️ Evaluated model performance

### 📌 4. Model Training & Evaluation
✔️ Built a function to:
   - Train models
   - Generate **confusion matrices**
   - Compute **accuracy, precision, recall, and F1-score**
✔️ Stored results in a dataframe for comparison
✔️ Visualized results using **grouped bar plots & heatmaps**

---

## 📈 Results & Insights
- **Class Imbalance:** Addressed using **SMOTE**
- **Best Performing Models:** [Specify best models and their accuracy]
- **Key Features Affecting Failures:** [Specify important features]
- **Performance Improvements:** Hyperparameter tuning + SMOTE led to better classification

---

## ⚙️ How to Run the Project
1. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn
   ```
2. Run the Jupyter Notebook step-by-step.
3. Observe model performance and predictions.

---

## 🛠️ Tools & Libraries Used
- **Python**
- **Pandas, NumPy** - Data Handling
- **Matplotlib, Seaborn** - Data Visualization
- **Scikit-learn** - Machine Learning Models
- **Imbalanced-learn (SMOTE)** - Handling Class Imbalance

---

## 🔥 Key Takeaways
✔️ **Class Balancing Techniques** (SMOTE) improve performance on imbalanced datasets.
✔️ **Binary vs. Multi-Class Classification** require different evaluation strategies.
✔️ **Confusion Matrices & Bar Plots** help visualize model performance.
✔️ **Reusable ML Functions** make experimentation easier and efficient.

---

🚀 **This project demonstrates how machine learning enhances predictive maintenance by analyzing sensor data. Open for future improvements!**

