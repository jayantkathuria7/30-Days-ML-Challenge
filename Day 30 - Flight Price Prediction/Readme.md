# Flight Price Predictor

## Overview
This project aims to predict flight ticket prices using various machine learning models. The dataset used contains details of flight bookings such as airline, departure time, duration, and price. The goal is to build a model that accurately estimates flight prices based on these features.

## Dataset
- **Source**: [Flight Price Prediction Dataset](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction?select=Clean_Dataset.csv)
- The dataset consists of structured data with flight details such as airline, departure time, duration, source, destination, and ticket prices.

## Kaggle Notebook
You can find the full implementation in the Kaggle notebook: [Flight Price Prediction](https://www.kaggle.com/code/jayantkathuria/flight-price-prediction)

## Approach
1. **Data Preprocessing**:
   - Handled missing values
   - Converted categorical features into numerical values using one-hot encoding
   - Scaled numerical features for better model performance

2. **Feature Engineering**:
   - Extracted useful information such as time of travel
   - Removed irrelevant columns

3. **Model Training**:
   - Implemented multiple machine learning models to predict flight prices
   - Evaluated models using R2 Score and Mean Squared Error (MSE)

## Model Performance
The following models were trained and evaluated:

| Model                   | R2 Score | Mean Squared Error |
|-------------------------|----------|--------------------|
| Linear Regression      | 0.905241  | 0.003257          |
| Decision Tree          | 0.983788  | 0.000557          |
| Random Forest         | 0.989983  | 0.000344          |
| Gradient Boosting     | 0.957768  | 0.001452          |
| Multi-Layer Perceptron | -4.811594 | 0.199760          |

## Conclusion
- The **Random Forest** model performed the best with an **R2 score of 0.9899** and the **lowest Mean Squared Error**.
- The **Decision Tree** model also performed well but was slightly less accurate than Random Forest.
- The **Linear Regression** model gave decent results but was outperformed by ensemble methods.
- The **Multi-Layer Perceptron** did not perform well, possibly due to improper hyperparameter tuning or data constraints.

## Future Improvements
- Fine-tuning hyperparameters for better model performance
- Exploring deep learning approaches for flight price prediction
- Adding more features such as weather, seasonal demand, and airline promotions

---

This project demonstrates how machine learning can be effectively used for predicting flight prices based on historical data. 🚀

