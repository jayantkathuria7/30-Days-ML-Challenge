# Stock Price Prediction Using ARIMA

## Overview
This project focuses on predicting stock prices using the **ARIMA (AutoRegressive Integrated Moving Average)** model. The goal is to analyze historical stock price data, apply time-series forecasting techniques, and visualize the predicted stock prices.

## Dataset
- The dataset used in this project contains historical stock price data, including date, price, and other relevant financial indicators.
- Data Source: [Kaggle](https://www.kaggle.com/datasets/mhassansaboor/uber-stocks-dataset-2025)

## Steps Performed

### 1. Data Preprocessing
- Loaded the dataset and handled missing values.
- Converted date columns into proper datetime format.
- Performed basic exploratory data analysis (EDA).

### 2. Time Series Analysis
- Checked for **stationarity** using the **Augmented Dickey-Fuller (ADF) Test**.
- Applied **seasonal decomposition** to make the data stationary.

### 3. ARIMA Model Implementation
- Identified the optimal ARIMA parameters (**p, d, q**) using **Auto ARIMA**.
- Trained the ARIMA model on historical stock prices.
- Made future predictions and evaluated model performance.

### 4. Visualization & Interpretation
- Plotted actual vs predicted stock prices to analyze performance.
- Conducted **residual analysis** to ensure model assumptions were met.

## Tools & Libraries Used
- **Pandas**: Data manipulation and preprocessing
- **Matplotlib & Seaborn**: Data visualization
- **Statsmodels**: ARIMA model implementation
- **Scikit-learn**: Data processing utilities

## Key Learnings
- Importance of **stationarity** in time-series forecasting.
- How to determine **ARIMA parameters** manually or using Auto ARIMA.
- Understanding **residual analysis** for model validation.
- Limitations of ARIMA for financial time series and potential alternatives.

## Results
- The ARIMA model was able to capture trends in stock prices but has limitations in handling sudden market fluctuations.
- Future work could involve **LSTMs, Prophet, or hybrid models** for improved forecasting.

## How to Run the Project
1. Install the required libraries:  
   ```bash
   pip install pandas numpy matplotlib seaborn statsmodels
   ```
2. Open the Jupyter Notebook and run the cells sequentially.
3. Observe the visualizations and predictions.

## Resources Used
- [Statsmodels ARIMA Documentation](https://www.statsmodels.org/stable/tsa.html)
- [Time Series Forecasting Guide](https://www.machinelearningmastery.com/time-series-forecasting/)

---
This project is part of my **Machine Learning Challenge**, where I implement different ML techniques in 30 days. 🚀

