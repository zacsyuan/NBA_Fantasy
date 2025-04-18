# NBA_Fantasy
Capstone- NBA Player Injury Knowledge for NBA Fantasy Game Use

## 📁 Project Overview:



### 1. `DBSCAN.ipynb`
- Implements **DBSCAN clustering** using NBA player on-court performance and bio data
- Covers seasons from **2019 to 2024**.
- Visualizes natural clusters of player performance patterns.

### 2. `Risk Tier Profiling.ipynb`
- Calculates a **risk score** for each player based on five SHAP-identified key features.
- Uses **standardized scores** and statistical thresholds to classify players into:
  - **High Risk**
  - **Medium Risk**
  - **Low Risk**
- Output risk tiers are used in the Streamlit dashboard.

### 3. `Streamlit_Project_Fantasy_Basketball_Risk_Profiling.py`
- Builds an **interactive Streamlit dashboard** to display player risk tiers.
- Based on **2024-25 season data** (as of April 4, 2025).
- Enables filtering by player, team, and position.


## 📊 Key Technologies
- Python (pandas, scikit-learn, SHAP, Xgboost, Streamlit, Seborn, Numpy)
- Clustering: **DBSCAN**
- Modeling & Predicton:**XGboost**
- Visualization: **Streamlit**
- Data: NBA player performance & bio data (2019–2025)


## 🚀 Live Dashboard

👉 Explore the dashboard here:  
**[NBA Fantasy Injury Risk Dashboard](https://nbafantasy-lcddcz9dxmxunjfop42qn8.streamlit.app/)**



## ✍️ Author
Created by ** Jialee Huang, Zac Sheng Yuan** | 2025 Apr  
