# Household Power Consumption Prediction

## Dataset
- **Source:** [UCI Machine Learning Repository - Individual Household Electric Power Consumption](https://archive.ics.uci.edu/ml/datasets/individual+household+electric+power+consumption)
- **Description:** This dataset contains measurements of electric power consumption in a single household over time. The goal is to perform **basic univariate time series analysis** to predict future power consumption.

## Objective
- Learn the basics of time series analysis by working with real-world energy consumption data.
- Develop a simple forecasting model using past power consumption trends.

## 1. Data Preprocessing
- **Datetime Handling:** Converted timestamps into proper datetime format.
- **Missing Values:** Used forward fill to handle missing values.
- **Feature Selection:** Focused on **Global_active_power** as the main variable for prediction.
- **Resampling:** Aggregated data into daily intervals to reduce noise.

## 2. Exploratory Data Analysis (EDA)
- **Trend Analysis:** Found that power consumption has seasonal patterns.
- **Peak Usage Hours:** Higher usage observed in the evening.
- **Weekday vs. Weekend Trends:** Noticed small differences in power usage.
- **Outliers:** Removed extreme values that could affect the model.

## 3. Time Series Modeling
- **Stationarity Check:** Used the ADF test and applied differencing to make the data stationary.
- **Models Tried:**
  - **ARIMA (AutoRegressive Integrated Moving Average)**
- **Model Evaluation:** Evaluated model based on RMSE.

## 4. Key Learnings
- **Trend and Seasonality:** Observed repeating patterns in power consumption.
- **Best Performing Model:** ARIMA gave decent results for short-term forecasting.
- **Challenges:** Data preprocessing and making the series stationary were tricky.

## 5. Next Steps
- Try adding external factors like temperature to improve predictions.
- Experiment with deep learning models like LSTM in the future.
- Learn more about hyperparameter tuning for ARIMA.

## 6. Tools Used
- **Python Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Statsmodels, Scikit-learn

### Summary:
This project was my first step into time series analysis. I learned how to handle time-based data, check for stationarity, and apply basic forecasting models like ARIMA and moving averages. There is still a lot to explore, but this was a great start!

