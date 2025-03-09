# Airline Passenger Satisfaction Prediction

## Scope of the Project
This project aims to analyze passenger satisfaction in airlines using machine learning models. By leveraging a dataset containing various features related to passenger experience, we train models to predict whether a passenger is satisfied or dissatisfied with the airline service.

## Dataset
The dataset used for this project was obtained from Kaggle: [Airline Passenger Satisfaction Dataset](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction). It includes features such as:
- **Passenger Type** (Loyal, Disloyal, etc.)
- **Class of Travel** (Business, Economy, Economy Plus)
- **Flight Distance**
- **Inflight Service Ratings**
- **Seat Comfort**
- **Inflight WiFi Service**
- **Check-in Service**
- **On-board Experience Ratings**
- **Customer Satisfaction** (Target variable: 0 = Dissatisfied, 1 = Satisfied)

## Project Steps

### 1. Data Preprocessing
- Checked for missing values and handled them accordingly.
- Converted categorical features into numerical representations.
- Standardized numerical features for better model performance.
- Splitted the dataset into **training** and **testing** sets.

### 2. Exploratory Data Analysis (EDA)
- Visualized the distribution of satisfied vs. dissatisfied passengers.
- Analyzed correlations between different features and passenger satisfaction.
- Examined the impact of service ratings on passenger experience.

### 3. Machine Learning Models Used
The following models were trained and evaluated:
1. **Logistic Regression** - Accuracy: 87.39%
2. **Decision Tree Classifier** - Accuracy: 94.57%
3. **Random Forest Classifier** - Accuracy: 94.57%
4. **Support Vector Machine (SVM)** - Accuracy: 95.72%
5. **Multi-Layer Perceptron (MLP - Neural Network)** - Accuracy: 95.99%

### 4. Model Performance & Best Model
- The **Multi-Layer Perceptron (MLP)** model achieved the highest accuracy of **95.99%**, outperforming other models.
- **SVM** was the second-best performing model with an accuracy of **95.72%**.
- **Logistic Regression** had the lowest accuracy due to its linear nature, which might not capture complex patterns in passenger behavior.
- **Decision Tree and Random Forest** performed similarly, indicating that ensemble learning improved individual decision tree performance.

## Libraries & Resources Used
- **Python**
- **NumPy & Pandas** (Data handling and preprocessing)
- **Scikit-learn** (Machine learning models, feature scaling, and evaluation)
- **Matplotlib & Seaborn** (Data visualization)

## How to Use
1. Clone the repository and navigate to the project folder:
   ```sh
   git clone <repo-link>
   cd Airline-Passenger-Satisfaction
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
This project demonstrates the use of various machine learning models to predict airline passenger satisfaction. The **MLP model** performed best, highlighting the importance of deep learning approaches in handling complex relationships in customer experience data.

---
