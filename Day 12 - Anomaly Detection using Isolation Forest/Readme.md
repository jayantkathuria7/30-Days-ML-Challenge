# Anomaly Detection using Isolation Forest

This project focuses on detecting anomalies in a dataset using the Isolation Forest algorithm, a popular unsupervised learning technique for identifying rare and suspicious data points.

---

## 📚 **Dataset Description**
The dataset used contains various features related to transactions, with anomalies indicating potential fraudulent or rare events. The features were processed before applying anomaly detection techniques.

**Dataset Link:** [Bank Transaction Dataset for Fraud Detection](https://www.kaggle.com/datasets/valakhorasani/bank-transaction-dataset-for-fraud-detection)

---

## 🔄 **Project Workflow**

### 1. **Data Preprocessing**
- Loaded the dataset and performed basic exploratory data analysis (EDA).
- Handled missing values and standardized numerical features.
- Applied **Principal Component Analysis (PCA)** for dimensionality reduction to visualize results effectively.

### 2. **Anomaly Detection with Isolation Forest**
- Used **Isolation Forest** to detect anomalies by identifying points that are easier to isolate.
- Assigned anomaly scores to each data point.
- Labeled points with high anomaly scores as fraud/anomalies.

### 3. **Visualization & Interpretation**
- Reduced the dataset to two principal components using **PCA** for visualization.
- Plotted anomalies (fraudulent points) in red and normal transactions in blue.
- Interpreted clusters and anomaly distribution in the visual representation.

---

## ⚙️ **How to Run the Project**
1. **Clone the Repository**
```bash
git clone <repository-url>
```

2. **Navigate to the Project Directory**
```bash
cd anomaly-detection
```

3. **Install Required Libraries**
```bash
pip install -r requirements.txt
```

4. **Run the Jupyter Notebook**
```bash
jupyter notebook
```

---

## 📚 **Resources Used**
- **Python Libraries:**
  - `pandas` for data manipulation
  - `numpy` for numerical operations
  - `matplotlib` and `seaborn` for visualizations
  - `scikit-learn` for PCA and Isolation Forest
- **Machine Learning Concepts:**
  - Isolation Forest for anomaly detection
  - PCA for dimensionality reduction
  
---

## ✅ **Key Takeaways**
- **Isolation Forest** effectively detected anomalies in the dataset.
- **PCA visualization** helped in understanding the separation of normal vs anomalous points.
- The method can be extended to real-world fraud detection and security monitoring applications.

---


