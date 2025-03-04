# 🔬 Breast Cancer Prediction using Machine Learning

## 📌 Overview
This project focuses on predicting whether a breast cancer tumor is **benign (B)** or **malignant (M)** using machine learning models. The dataset is obtained from **[Kaggle's Breast Cancer Dataset](https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset)** and contains various features extracted from tumor images.

The project explores multiple models, evaluates their performance, and determines the most accurate classifier.

## 📂 Dataset
- **Source:** [Kaggle](https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset)
- **Features:**
  - Mean, standard error, and worst values of cell nuclei characteristics
  - Radius, texture, perimeter, area, smoothness, compactness, symmetry, and fractal dimension
- **Target Variable:** Diagnosis (B = Benign, M = Malignant)

### Dataset Distribution
The dataset contains **62.7% benign** and **37.3% malignant** cases.

![Dataset Distribution](Dataset%20Distribution.png)

## 🛠️ Technologies Used
- **Programming Language:** Python
- **Libraries & Frameworks:**
  - `NumPy`, `Pandas` – Data manipulation
  - `Matplotlib`, `Seaborn` – Data visualization
  - `Scikit-learn` – Model training & evaluation
  - `XGBoost` – Advanced boosting technique

## 🚀 Installation & Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```
4. Open `Breast_Cancer_Prediction.ipynb` and run the cells sequentially.

## 🔍 Methodology
1. **Data Preprocessing**:
   - Handling missing values
   - Feature selection
   - Data normalization
2. **Model Training**:
   - Logistic Regression
   - Random Forest
   - Decision Tree
   - XGBoost
   - Gradient Boosting
3. **Evaluation Metrics**:
   - Accuracy Score
   - F1 Score (for class imbalance handling)
   - Confusion Matrix

## 📈 Results

### F1 Score Comparison
Below is a comparison of the F1 scores for both **Benign (B)** and **Malignant (M)** predictions across 5 models:

![F1 Score Comparison across 5 Models](F1%20Score%20Comparison%20across%205%20Models.png)

### Model Accuracy Comparison
The **Logistic Regression model** performed the best, achieving **97% accuracy**, while **XGBoost** and **Random Forest** also performed well.

![Model Accuracy Comparison](Model%20Accuracy%20Comparison.png)

## 🔥 Key Insights
- **Logistic Regression outperformed** other models, making it a simple yet effective choice.
- **XGBoost performed well**, but required tuning to avoid overfitting.
- **Random Forest & Decision Trees** were slightly less accurate due to overfitting on training data.

## 📜 Future Work
- Implement **Deep Learning models** (CNNs) to analyze tumor images.
- Perform **hyperparameter tuning** for better model optimization.
- Deploy the model using a **Flask/Django web app** for real-world use.

## 🤝 Contributing
Contributions are welcome! If you want to improve the project, feel free to fork the repository and submit a pull request.

---
**Dataset:** [Kaggle Breast Cancer Dataset](https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset)  
**Contact:** [Your Email / GitHub Profile]
```
