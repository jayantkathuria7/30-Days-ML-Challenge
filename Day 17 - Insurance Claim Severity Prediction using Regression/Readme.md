# Insurance Claim Severity Prediction using Regression

## Overview
This project aims to predict the severity of insurance claims using various regression models. Due to hardware constraints, the analysis was conducted on a reduced dataset (approximately 45% of the original data) to optimize computational efficiency.

## Methodology
1. **Data Preprocessing:**
   - One-hot encoding was applied to categorical columns to convert them into numerical features.
   - Principal Component Analysis (PCA) was used for dimensionality reduction, improving model efficiency.

2. **Model Training:**
   - The following regression models were implemented and compared:
     - Linear Regression
     - Decision Tree Regressor
     - Random Forest Regressor
     - Gradient Boosting Regressor
     - Multi-Layer Perceptron (MLP)
     - Neural Network (Deep Learning Model)

3. **Evaluation Metrics:**
   - **R² Score:** Measures the proportion of variance explained by the model.
   - **Mean Squared Error (MSE):** Measures the average squared difference between actual and predicted values.

## Results
| Model                  | R² Score | Mean Squared Error |
|------------------------|----------|---------------------|
| Linear Regression      | 0.502630 | 0.323704            |
| Decision Tree         | 0.293797 | 0.459619            |
| Random Forest        | 0.387027 | 0.398942            |
| Gradient Boosting    | 0.516169 | 0.314892            |
| Multi-Layer Perceptron | 0.371930 | 0.408767            |
| Neural Network       | 0.507727 | 0.320387            |

### Key Observations:
- Gradient Boosting achieved the **highest R² score (0.516)** and the **lowest MSE (0.3149)**, making it the most effective model in this case.
- The Neural Network model performed comparably to Linear Regression but did not surpass Gradient Boosting.
- Decision Trees had the **lowest performance**, likely due to overfitting and lack of generalization.

## Challenges & Learnings
- Due to **hardware limitations**, a smaller dataset was used to reduce computational time.
- PCA helped in **dimensionality reduction**, improving model performance and efficiency.
- Gradient Boosting proved to be a **strong candidate** for insurance claim severity prediction.

## Future Improvements
- Experiment with **hyperparameter tuning** for Random Forest and Neural Networks to optimize performance.
- Implement **feature selection techniques** to improve model interpretability.
- Explore additional models such as **XGBoost or LightGBM** for better performance.

## Repository Structure
```
├── data/                # Dataset (if applicable)
├── models/              # Saved models
├── notebooks/           # Jupyter notebooks
├── src/                 # Source code
├── results/             # Output results and visualizations
├── README.md            # Project documentation
```

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/insurance-claim-severity.git
   cd insurance-claim-severity
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter notebook:
   ```bash
   jupyter notebook
   ```
4. Execute the notebook to train models and evaluate results.

## Acknowledgments
This project was developed as part of my **Machine Learning practice** to explore regression techniques and model evaluation strategies.

---
Feel free to reach out for collaborations or discussions!

