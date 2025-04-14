import streamlit as st

import pandas as pd

import numpy as np










#file_path = r'D:\MADS\Capstone\
df_prep = pd.read_csv('2024-2025_NBA as of Apr.csv')

df_Features=df_prep[['PLAYER_NAME','POSITION','TEAM_ABBREVIATION','EXP','FGM','STL','PFD','AST']]
df_Features=df_Features.dropna(subset=['EXP'])
df_Features['EXP'] = df_Features['EXP'].replace('R', 0.5)
df_Features['EXP'] = pd.to_numeric(df_Features['EXP'], errors='coerce')
df_Features = df_Features.rename(columns={'TEAM_ABBREVIATION': 'TEAM'})

weights = {
    'EXP': 0.36,
    'FGM': 0.27,
    'STL': 0.13,
    'PFD': 0.12,
    'AST': 0.12
}

df_Features['risk_score'] = (
    df_Features['EXP'] * weights['EXP'] +
    df_Features['FGM'] * weights['FGM'] +
    df_Features['STL'] * weights['STL'] +
    df_Features['PFD'] * weights['PFD'] +
    df_Features['AST'] * weights['AST']
)


# df_Features['injury_risk'] = pd.qcut(
#     df_Features['risk_score'], 
#     q=3, 
#     labels=['Low', 'Medium', 'High']
# )

mean = df_Features['risk_score'].mean()
std = df_Features['risk_score'].std()


def classify_risk(score):
    if score > mean + std:
        return 'High'
    elif score < mean - std:
        return 'Low'
    else:
        return 'Medium'

df_Features['INJ RISK'] = df_Features['risk_score'].apply(classify_risk)

####Dashboard Build


st.title("🏀 NBA Player Injury Risk Dashboard as of Apr 9th_2024-25 Season")
st.sidebar.header("🔍 Filter Panel")




# Initialize session state for filters
for key in ['selected_risk', 'selected_player','selected_position','selected_team']:
    if key not in st.session_state:
        st.session_state[key] = 'All'

# Handle Clear Filters button
if st.sidebar.button("🔄 Clear Filters"):
    st.session_state.selected_risk = 'All'
    st.session_state.selected_player = 'All'
    st.session_state.selected_position = 'All'
    st.session_state.selected_team = 'All'

# Dropdown options
injury_options = ['All'] + sorted(df_Features['INJ RISK'].unique().tolist())
player_options = ['All'] + sorted(df_Features['PLAYER_NAME'].unique().tolist())
position_options = ['All'] + sorted(df_Features['POSITION'].unique().tolist())
team_options = ['All'] + sorted(df_Features['TEAM'].unique().tolist())

# Use session state to reset filters
selected_risk = st.sidebar.selectbox(
    "Select Injury Risk",
    injury_options,
     index=injury_options.index(st.session_state.selected_risk),
    key='selected_risk'
)

selected_player = st.sidebar.selectbox(
    "Select Player",
    player_options,
     index=player_options.index(st.session_state.selected_player),
    key='selected_player'
)

selected_position = st.sidebar.selectbox(
    "Select Position",
    position_options,
    index=position_options.index(st.session_state.selected_position),
    key='selected_position'
)

selected_team = st.sidebar.selectbox(
    "Select Team",
    team_options,
    index=team_options.index(st.session_state.selected_team),
    key='selected_team'
)





filtered_df = df_Features.copy()

if selected_risk != 'All':
    filtered_df = filtered_df[filtered_df['INJ RISK'] == selected_risk]

if selected_player != 'All':
    filtered_df = filtered_df[filtered_df['PLAYER_NAME'] == selected_player]

if selected_position != 'All':
    filtered_df = filtered_df[filtered_df['POSITION'] == selected_position]

if selected_team != 'All':
    filtered_df = filtered_df[filtered_df['TEAM'] == selected_team]

# Show table
st.subheader("📊 Filtered Player List")
st.dataframe(filtered_df.reset_index(drop=True))
