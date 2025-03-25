# Sentiment Analysis on Twitter Dataset

## 📌 Project Overview
This project focuses on **Sentiment Analysis** using machine learning techniques to classify tweets as positive or negative. Due to hardware limitations, a **smaller subset of the dataset** was used for training and evaluation.

---

## 📂 Dataset Information

🔗 **Project Notebook on Kaggle:** [Click Here](https://www.kaggle.com/code/jayantkathuria/sentiment-analysis-on-twitter-dataset)

- **Source:** Twitter dataset containing labeled sentiment data.[Click Here](https://www.kaggle.com/datasets/kazanova/sentiment140)
- **Classes:** Binary classification (Positive, Negative)
- **Subset Used:** Reduced dataset for optimized processing.

---

## 🔄 Text Preprocessing
✔️ Converted text to **lowercase**
✔️ Removed **URLs**
✔️ Removed **numbers**
✔️ **Tokenized** text into words
✔️ Removed **stopwords** & **punctuation**
✔️ Applied **stemming** (e.g., "running" → "run")
✔️ Handled **repeating characters** (e.g., "soooon" → "soon")

---

## 🏗️ Model Training & Evaluation
### **Machine Learning Models Used:**
- **Logistic Regression**
- **Decision Tree**
- **Random Forest**
- **Gradient Boosting**
- **XGBoost**
- **Support Vector Machine (SVM)**

### **Performance Metrics**
| Model | Train Accuracy | Test Accuracy | F1 Score (Class 0) | F1 Score (Class 1) | Precision (Class 0) | Precision (Class 1) | Recall (Class 0) | Recall (Class 1) |
|--------|---------------|--------------|--------------------|--------------------|--------------------|--------------------|------------------|------------------|
| Logistic Regression | 80.73% | 74.83% | 74.76% | 74.91% | 76.21% | 73.52% | 73.36% | 76.36% |
| Decision Tree | 98.96% | 67.77% | 67.70% | 67.83% | 68.95% | 66.63% | 66.50% | 69.07% |
| Random Forest | 98.96% | 73.00% | 72.91% | 73.09% | 74.35% | 71.71% | 71.52% | 74.52% |
| Gradient Boosting | 70.02% | 68.38% | 62.20% | 72.83% | 79.19% | 63.09% | 51.21% | 86.11% |
| XGBoost | 78.38% | 71.62% | 69.15% | 73.71% | 77.19% | 67.70% | 62.63% | 80.89% |
| SVM | 93.76% | 74.72% | 74.38% | 75.05% | 76.64% | 72.95% | 72.24% | 77.27% |

---

## 📈 Insights & Findings
- **Logistic Regression & SVM** provided the most balanced performance.
- **Decision Trees & Random Forest** overfitted on training data.
- **Gradient Boosting & XGBoost** showed promise but require further tuning.
- The smaller dataset limited generalization; using a larger dataset could improve performance.

---

## ⚙️ How to Run the Project
1. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn xgboost nltk
   ```
2. Run the Jupyter Notebook step-by-step.
3. Observe model performance and predictions.

---

## 🛠️ Tools & Libraries Used
- **Python**
- **Pandas, NumPy** - Data Handling
- **Matplotlib, Seaborn** - Data Visualization
- **NLTK** - Text Processing
- **Scikit-learn, XGBoost** - Machine Learning Models

---

🚀 **This project demonstrates the use of ML models for sentiment analysis on Twitter data. Future improvements include hyperparameter tuning and training on a larger dataset.**

