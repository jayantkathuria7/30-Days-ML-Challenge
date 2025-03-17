# Obesity Pattern Clustering

This project focuses on clustering individuals based on lifestyle and health-related attributes to identify patterns related to obesity levels. Using unsupervised machine learning techniques, the project categorizes data points into distinct groups to derive insights about obesity patterns.

---

## 📚 **Dataset Description**

The dataset was sourced from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition). It contains various attributes related to health, habits, and lifestyle, including:

- **Gender**: Gender of the individual  
- **Age**: Age of the individual  
- **Height**: Height in meters  
- **Weight**: Weight in kilograms  
- **family_history_with_overweight**: Family history of obesity (Yes/No)  
- **FAVC**: Frequency of consuming high-calorie foods  
- **FCVC**: Frequency of consuming vegetables  
- **NCP**: Number of main meals consumed daily  
- **CAEC**: Frequency of food consumption between meals  
- **SMOKE**: Smoking habits (Yes/No)  
- **CH2O**: Amount of water intake daily  
- **SCC**: Monitoring of daily calorie intake (Yes/No)  
- **FAF**: Frequency of physical activity  
- **TUE**: Time spent using technological devices  
- **CALC**: Frequency of alcohol consumption  
- **MTRANS**: Mode of transportation  

---

## 🔄 **Project Workflow**

### 1. **Data Preprocessing**
- Removed missing values and ensured data consistency.
- Applied label encoding to convert categorical variables into numerical format.
- Used standardization for feature scaling to ensure uniformity.

### 2. **Exploratory Data Analysis (EDA)**
- Analyzed data distributions through basic visualizations.
- Observed relationships between various features and obesity levels.

### 3. **Clustering Approach**
- **Algorithm Used:** Applied K-Means clustering to group the data points.
- **Choosing Number of Clusters:** Used the Elbow Method to determine the optimal number of clusters.
- **Visualization:** Visualized clusters using a 2D plot to understand separation.

### 4. **Results & Insights**
- Identified distinct lifestyle-based clusters that highlight patterns related to obesity.
- Provided brief insights into the common characteristics within each cluster.

---

## ⚙️ **How to Run the Project**
1. **Clone the Repository**
```bash
git clone <repository-url>
```

2. **Navigate to the Project Directory**
```bash
cd obesity-clustering
```

3. **Install Required Libraries**
```bash
pip install -r requirements.txt
```

4. **Run the Jupyter Notebook**
```bash
jupyter notebook
```


## 📚 **Resources Used**
- **Dataset:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition)
- **Python Libraries:**
  - `pandas` for data manipulation
  - `numpy` for numerical operations
  - `matplotlib` and `seaborn` for visualizations
  - `scikit-learn` for clustering and evaluation metrics

---

## ✅ **Key Takeaways**
- K-Means clustering helped categorize individuals into distinct lifestyle patterns related to obesity.
- The Elbow Method and Silhouette Score were useful in validating the cluster quality.

---

