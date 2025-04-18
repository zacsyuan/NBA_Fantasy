# NBA_Fantasy
Capstone- NBA Player Injury Knowledge for NBA Fantasy Game Use

## 📁 Project Overview:
Fantasy Basketball game is one of the most popular platforms for basketball enthusiasts to build and manage their own virtual teams, competing based on real-life player performances. A critical factor that influences a team’s success is player availability—once a player is injured, they contribute no stats, significantly impacting a fantasy team’s win rate. However predicting injuries is notoriously diffucult, leaving fantasy players/managers struggling to balance risk and reward when drafting their rosters. 

In this project, we aim to identify useful risky factors and patterns to provide a guideline for fantasy players to quantify players’ injury risk. We connect each player’s seasonal performance metrics, including rebounds, blocks, minutes played, and player’s physical statistics, with their total game missed due to injury. We use both supervised and unsupervised machine learning methods, including XGBoost and DBSCAN, to explore which factors are most predictive of injury risk. Our project explores beyond known common sense, such as the more you play, the more likely you are to injure yourself. It uncovers some additional interesting patterns that contribute to injuries, for example, players with more assists may also be prone to have longer injury duration, because assists reflect high involvement in gameplay and workload. These insights can help fantasy players make more informed decisions, strategically selecting players who combine strong performance with lower injury risk.


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
