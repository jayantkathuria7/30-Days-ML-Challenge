# House Price Prediction Using Time Series Analysis  

## Overview  
This notebook focuses on analyzing time series data to predict home prices across U.S. metropolitan regions. The dataset contains historical home values, and the analysis includes handling missing values, converting the data into a time series format, and visualizing long-term trends.  

## Dataset  
- **Source:** [Zillow Research Data](https://www.zillow.com/research/data/)  
- **Description:** Contains historical monthly home values for various metropolitan regions in the U.S.  

## Key Steps & Analysis  

### 1. Data Loading & Inspection  
- **Columns:** The dataset includes metadata (`RegionID`, `SizeRank`, `RegionName`) and monthly home values from **2000-01-31** to **2025-02-28**.  
- **Shape:** 895 rows (regions) and 307 columns (metadata + monthly values).  

### 2. Missing Value Handling  
- **Total Missing Values:** 49,267.  
- **Observation:**  
  - Older dates (e.g., 2000-01-31) have more missing values (464 missing).  
  - Missing values gradually decrease over time, with recent dates (2020 onward) having minimal or no missing values.  
- **Solution:**  
  - Used **backward fill** (`df.backfill(axis=1)`) to propagate future values backward.  
  - Applied **forward fill** (`fillna(method='ffill')`) to ensure no missing values remain.  

### 3. Time Series Conversion  
- **Reshaping:** Transposed the dataset to make dates rows and regions columns.  
- **Datetime Indexing:** Converted the index to datetime format for time series analysis.  

### 4. Data Visualization  
- **Region-specific Plots:** Attempted to visualize individual regions like "San Diego, CA", but skipped due to insufficient data.  
- **Overall U.S. Trend:** Successfully plotted the aggregated U.S. home price trend from **2000 to 2025** to analyze long-term market behavior.  

## Summary  
This analysis prepared the dataset for time series forecasting by:  
✅ Handling missing values effectively.  
✅ Transforming the data into a structured time series format.  
✅ Visualizing historical trends in home values.  

### Potential Next Steps  
🔹 Explore seasonal trends and stationarity in home prices.  
🔹 Apply predictive modeling (ARIMA, LSTM, etc.) for forecasting.  
