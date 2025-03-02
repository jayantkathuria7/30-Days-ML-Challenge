# Iris Flower Classification 🌸

## 📌 Overview
This project focuses on **Iris Flower Classification**, a classic **multi-class classification problem** in machine learning. The goal is to predict the species of an iris flower based on four key features:
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

We utilize multiple machine learning models and compare their performances using evaluation metrics.

## 📊 Dataset
- **Source**: [UCI Machine Learning Repository - Iris Dataset](https://archive.ics.uci.edu/dataset/53/iris)
- **Classes**: 3 categories of iris flowers:
  - **Setosa**
  - **Versicolor**
  - **Virginica**
- **Features**:
  - Sepal length (cm)
  - Sepal width (cm)
  - Petal length (cm)
  - Petal width (cm)
- **Total Samples**: 150 (50 per class)

## 🛠️ Implementation Steps
### 1️⃣ Data Preprocessing
- **Loaded dataset** using Pandas
- **Checked for missing values** (No missing data found)
- **Exploratory Data Analysis (EDA)**
  - Pairplot visualization using Seaborn
  - Feature distributions for each class

### 2️⃣ Data Splitting & Scaling
- **Train-Test Split**: 80% training, 20% testing
- **Standardized features** using `StandardScaler` to improve model performance

### 3️⃣ Model Selection & Training
We implemented and evaluated the following machine learning models:
- **Logistic Regression**
- **Decision Tree Classifier**
- **K-Nearest Neighbors (KNN)**
- **Random Forest Classifier**

### 4️⃣ Model Evaluation
We evaluated the models using the following metrics:
- **Accuracy Score**
- **Classification Report** (Precision, Recall, F1-Score)
- **Confusion Matrix** for error analysis

## 📈 Results
| Model                | Accuracy |
|----------------------|----------|
| Logistic Regression | 97%      |
| Decision Tree       | 96%      |
| KNN (k=5)           | 96%      |
| Random Forest       | 98%      |

**🔹 Random Forest achieved the highest accuracy of 98%!** 🎯

## 🚀 Future Improvements
- **Hyperparameter Tuning** (using `GridSearchCV` to optimize KNN & Decision Tree parameters)
- **Deploying the model** as a web application using Flask/Streamlit

## 📂 Repository Structure
```
├── Iris Flower Classification.ipynb   # Jupyter Notebook with full implementation
├── README.md                           # Project Documentation
├── iris.data                           # Raw dataset 
└── images/                             # Visualizations 
```

## 📌 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Iris-Flower-Classification.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Iris-Flower-Classification
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Jupyter Notebook to train models and visualize results.

## 💡 Conclusion
This project showcases **multi-class classification using machine learning**. By leveraging various models and evaluation techniques, we successfully built an **efficient iris species classifier**. 🚀

---

