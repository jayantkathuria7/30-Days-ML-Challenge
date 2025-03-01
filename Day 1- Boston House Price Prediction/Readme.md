# 🏡 Boston Housing Price Prediction

This project aims to predict house prices using various machine learning models. The dataset contains **506 rows** and **14 predictor variables** that describe different factors influencing housing prices in Boston.

## 📊 Dataset Description  

The dataset consists of the following 15 columns:

| Column    | Description |
|-----------|-------------|
| **CRIM**  | Per capita crime rate by town |
| **ZN**    | Proportion of residential land zoned for lots over 25,000 sq.ft. |
| **INDUS** | Proportion of non-retail business acres per town |
| **CHAS**  | Charles River dummy variable (1 if tract bounds river; 0 otherwise) |
| **NOX**   | Nitrogen oxide concentration (parts per 10 million) |
| **RM**    | Average number of rooms per dwelling |
| **AGE**   | Proportion of owner-occupied units built before 1940 |
| **DIS**   | Weighted distance to five Boston employment centers |
| **RAD**   | Index of accessibility to radial highways |
| **TAX**   | Property tax rate per $10,000 |
| **PTRATIO** | Pupil-teacher ratio by town |
| **B**     | 1000(Bk - 0.63)² where Bk is the proportion of Black residents |
| **LSTAT** | Percentage of lower-status population |
| **MEDV**  | Median value of owner-occupied homes in $1000s (Target variable) |

---

## 📈 Exploratory Data Analysis (EDA)

### 🔥 Correlation Heatmap
The correlation matrix reveals:
- **RM (number of rooms)** has a strong **positive** correlation with price.
- **LSTAT (lower-status percentage)** has a strong **negative** correlation.
- **NOX (pollution levels)** and **TAX (property tax rate)** also negatively impact prices.

📌 **Plot:**  
![Correlation Heatmap](plots/Correlation%20Heatmap.png)

---

## 🚀 Model Performance  

We trained multiple models to predict housing prices. Below is a comparison of their performance:

### **Error Comparison**
- **Gradient Boosting** performed the best with the **lowest error**.
- **SVM** performed the worst before scaling but improved significantly after scaling.

📌 **Error Before Scaling:**  
![Error for Different Models](plots/Error%20for%20Different%20Models.png)  

📌 **Error After Scaling:**  
![Error After Scaling](plots/Error%20After%20Scaling%20for%20Different%20Models.png)  

---

### **R² Score Comparison**
- **Gradient Boosting** achieved the highest R² score (~0.86 after scaling).
- **SVM** had the lowest R² score before scaling but improved post-scaling.

📌 **R² Before Scaling:**  
![R2 Scores for Different Models](plots/R2%20Scores%20for%20Different%20Models.png)  

📌 **R² After Scaling:**  
![R2 Scores After Scaling](plots/R2%20Scores%20After%20Scaling%20for%20Different%20Models.png)  

📌 **Comparison Before & After Scaling:**  
![Comparison](plots/comparison%20before%20and%20after%20scaling.png)  

---

## ⚙️ Installation & Usage

1️⃣ Clone the repository:  
```bash
git clone https://github.com/yourusername/Boston-Housing-ML.git
cd Boston-Housing-ML
```
## Install Dependencies

Run the following command to install the required dependencies:

```bash
pip install -r requirements.txt
```
## Future Improvements

- Try feature engineering (polynomial features, interaction terms).
- Implement hyperparameter tuning (GridSearchCV).
- Deploy the model using Flask or Streamlit.


