# Fake News Detection

## Overview
This project aims to detect fake news articles using machine learning models. The dataset used for training consists of labeled news articles categorized as either "Fake" or "Real." By applying Natural Language Processing (NLP) techniques and machine learning algorithms, this project effectively identifies misleading or false news.

## Dataset
The dataset used in this project was obtained from Kaggle: [Fake News Dataset](https://www.kaggle.com/datasets/vishakhdapat/fake-news-detection). It consists of labeled news articles with two classes:
- **Fake News** (1): News articles that contain misleading or false information.
- **Real News** (0): Authenticated and credible news articles.

## Machine Learning Models Used
Several machine learning models were applied to classify news articles:
1. **Support Vector Machine (SVM)**
2. **Logistic Regression**
3. **Random Forest Classifier**

## Project Workflow
1. **Data Preprocessing**
   - Removed unnecessary characters, punctuation, and stopwords.
   - Tokenized and vectorized text using **TF-IDF (Term Frequency-Inverse Document Frequency)**.
   
2. **Exploratory Data Analysis (EDA)**
   - Checked for class balance.
   - Visualized word distributions.

3. **Model Training & Evaluation**
   - Implemented multiple machine learning models.
   - Used **Accuracy, Precision, Recall, and F1-Score** to evaluate model performance.
   
4. **Best Performing Model**
   - The **Decision Tree** model achieved the highest accuracy (99.39%).

## Libraries & Resources Used
- **Python**
- **NumPy & Pandas** (Data handling and preprocessing)
- **Scikit-learn** (Machine learning models, TF-IDF, evaluation metrics)
- **Matplotlib & Seaborn** (Data visualization)

## How to Use
1. Clone the repository and navigate to the project folder:
   ```sh
   git clone <repo-link>
   cd Fake-News-Detection
   ```
2. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook to train models and evaluate performance:
   ```sh
   jupyter notebook
   ```

## Conclusion
This project successfully demonstrates how machine learning can be leveraged to detect fake news.
---

