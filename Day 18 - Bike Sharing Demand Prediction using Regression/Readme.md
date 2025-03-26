# Bike Sharing Demand Prediction

## Dataset
- **Source:** [UCI Machine Learning Repository - Bike Sharing Dataset](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset)
- **File Used:** `hour.csv`
- **Description:** Contains bike rental data with features such as datetime, season, temperature, humidity, windspeed, and the target variable `cnt` (total rentals).

## Model Performance
| Model                  | R² Score | Mean Squared Error |
|------------------------|----------|---------------------|
| Linear Regression      | 0.397950 | 19891.508845       |
| Decision Tree         | 0.878515 | 4013.823936        |
| Random Forest        | 0.934242 | 2172.615578        |
| Gradient Boosting    | 0.854284 | 4814.413072        |
| Multi-Layer Perceptron | 0.620745 | 12530.457122       |

## 1. Data Loading & Initial Exploration
- **Key Features:**
  - **Temporal:** `dteday` (date), `hr` (hour), `season`, `yr` (year), `mnth` (month)
  - **Weather:** `temp`, `atemp` (feels-like temperature), `hum` (humidity), `windspeed`
  - **User Type:** `casual` (non-registered), `registered`, `cnt` (total rentals)
- **Initial Checks:**
  - No missing values.
  - Data types: Mostly numerical, some categorical variables (`season`, `weathersit`).

## 2. Data Preprocessing
- **Categorical Mapping:** Converted numerical codes into readable labels (`season 1 → Winter`).
- **Datetime Conversion:** Parsed `dteday` into a datetime object.
- **Feature Categorization:**
  - `categorical_cols`: Season, weather, etc.
  - `numerical_cols`: Temperature, windspeed, etc.

## 3. Exploratory Data Analysis (EDA)
- **Seasonal Trends:** Higher rentals in fall, lower in winter.
- **Hourly Patterns:** Peaks at 8 AM and 5–6 PM (commute hours).
- **Weather Impact:** Clear weather significantly increased rentals.
- **User Behavior:** Registered users accounted for ~80% of rentals.
- **Temperature Correlation:** Positive correlation between temperature and rentals.
- **Outliers:** Addressed extreme values in windspeed using IQR.

## 4. Multicollinearity & Feature Selection
- **Correlation Matrix:** Dropped `temp` due to high correlation with `atemp` (r = 0.98).
- **VIF Analysis:** Confirmed no severe multicollinearity after removing redundant features.

## 5. Model Development
- **Algorithms Tested:**
  - Linear Regression (Baseline, R² = 0.39)
  - Decision Tree (R² = 0.74)
  - Random Forest (Best: R² = 0.84, MAE = 40.5, RMSE = 60.2)
  - Gradient Boosting (R² = 0.82)
- **Hyperparameter Tuning:** Applied to Decision Trees and Random Forest.

## 6. Key Findings
- **Top Features:** Hour of the day (`hr`), temperature (`temp`), and registered users were the most influential.
- **Time Dependency:** Rentals peak during morning and evening rush hours.
- **Weather Sensitivity:** Rain/snow reduced rentals by ~50% compared to clear weather.

## 7. Conclusion & Recommendations
- **Best Model:** Random Forest outperformed others due to its ability to capture non-linear relationships.
- **Next Steps:**
  - Incorporate external data (e.g., holidays, events).
  - Experiment with deep learning models (e.g., LSTM for temporal patterns).
  - Deploy the model for real-time demand prediction.

## 8. Tools Used
- **Python Libraries:** Pandas, Seaborn, Matplotlib, Scikit-learn

### Key Insight:
Time of day and weather are critical drivers of bike-sharing demand. Optimizing bike availability during peak hours and adverse weather can enhance user satisfaction.

