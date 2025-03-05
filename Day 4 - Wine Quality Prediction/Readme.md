# 🍷 Wine Quality Prediction

## 📌 Project Overview
This project aims to predict the quality of wine based on its physicochemical properties using various Machine Learning models. Due to a highly imbalanced dataset, the wine quality labels were grouped into two categories: **Good** and **Bad**.

## 📂 Dataset Information
- **Source:** [UCI Machine Learning Repository - Wine Quality Dataset](https://archive.ics.uci.edu/ml/datasets/wine+quality)
- **Features:** 11 numerical features (e.g., acidity, alcohol content, pH, etc.)
- **Target Variable:** Wine Quality (originally ranging from 3 to 8, later grouped into **Good** and **Bad** categories)
- **Imbalance:** Extreme imbalance, with some classes having as few as 9 samples

## ❓ Problem Statement
The goal is to develop an ML model that can accurately classify wine quality despite the dataset's imbalance.

## 🚀 Approach
1. **Data Preprocessing:**
   - Handled missing values
   - Scaled the numerical features
   - Created two target classes (Good & Bad) due to imbalance

2. **Model Training:**
   - Logistic Regression
   - Decision Tree Classifier
   - Random Forest Classifier
   - Support Vector Classifier (SVC)
   - XGBoost Classifier

3. **Evaluation Metrics:**
   - **Accuracy** (Train & Test)
   - **F1-Score for both classes** (to handle class imbalance)

## 📊 Results & Visualizations
- **Test Accuracy Comparison:** A bar plot was generated to compare the accuracy of different models.
- **F1-Score Analysis:** A grouped bar plot was created to show F1-scores for both the **Good** and **Bad** wine categories.

## ⚙️ Installation & Usage
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/wine-quality-prediction.git
cd wine-quality-prediction
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Jupyter Notebook
```bash
jupyter notebook
```
Open `Wine Quality Prediction.ipynb` and run the cells.

## 📈 Future Improvements
- **Hyperparameter Tuning** to improve model performance
- **Using SMOTE or Cost-Sensitive Learning** to handle imbalance
- **Deploying the model as a Web App** using Flask/Streamlit


## ⭐ Acknowledgments
- UCI Machine Learning Repository for the dataset
- Scikit-learn, XGBoost, and Matplotlib for ML and visualization

---
🔹 **If you found this project useful, don't forget to ⭐ the repo!**
```

