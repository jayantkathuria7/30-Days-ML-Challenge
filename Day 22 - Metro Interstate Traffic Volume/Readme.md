# Metro Interstate Traffic Volume Prediction

## Dataset Link
[Metro Interstate Traffic Volume Dataset](https://archive.ics.uci.edu/ml/datasets/Metro+Interstate+Traffic+Volume)

## Summary of Analysis

### 1. Initial Setup and Data Loading
- Imported necessary libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`.
- Suppressed warnings for a cleaner output.
- Loaded the dataset (`Metro_Interstate_Traffic_Volume.csv`) into a DataFrame (`df`).

### 2. Data Exploration
- Previewed the dataset using `df.head()`.
- Checked for missing values:
  - The `holiday` column had **99.87% missing values** and was dropped.
- Verified data types using `df.info()` to ensure consistency and no remaining missing values.

### 3. Feature Engineering
- Converted `date_time` into a **datetime index** for time-series analysis.
- Categorical Feature Analysis:
  - `weather_main`: Contains categories like **"Clouds", "Clear", "Mist", "Rain"**.
  - `weather_description`: More detailed weather conditions like **"scattered clouds"**.
- Separated columns into:
  - **Numerical Features**: `temp`, `rain_1h`, `snow_1h`, `clouds_all`, `traffic_volume`
  - **Categorical Features**: `weather_main`, `weather_description`

### 4. Key Observations
- **Traffic volume varies with weather and time-based factors**.
- **High missingness** in `holiday` made it unsuitable for analysis.
- **Potential correlations** between traffic patterns and weather conditions.

### 5. Next Steps
- **Visualizations**: Investigate relationships between weather and traffic volume.
- **Temporal Analysis**: Explore daily and weekly traffic patterns.
- **Predictive Modeling**: Build ML models using weather and time-based features.

## Insights
- The project is in an **exploratory phase**, mainly focusing on **data cleaning and understanding feature distributions**.
- Future work may include **advanced statistical analysis or machine learning** to predict traffic volume trends.

## Tools Used
- Python, Pandas, NumPy, Seaborn, Matplotlib

---
This README serves as a summary of the initial data exploration and cleaning steps. Further analysis can lead to valuable insights into traffic patterns and predictive modeling. 🚦📊

