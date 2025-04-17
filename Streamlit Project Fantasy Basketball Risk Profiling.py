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


#Standardize the feature values
from sklearn.preprocessing import StandardScaler
cols_to_scale = ['EXP', 'FGM', 'STL', 'PFD', 'AST']
scaler = StandardScaler()
df_scaled_values = scaler.fit_transform(df_Features[cols_to_scale])
df_scaled = pd.DataFrame(df_scaled_values, columns=cols_to_scale, index=df_Features.index)
df_Features_scaled = df_Features.copy()
df_Features_scaled[cols_to_scale] = df_scaled

#input the weight of the features computed by SHAP mean value
weights = {
    'EXP': 0.36,
    'FGM': 0.27,
    'STL': 0.13,
    'PFD': 0.12,
    'AST': 0.12
}

df_Features_scaled['risk_score'] = (
    df_Features_scaled['EXP'] * weights['EXP'] +
    df_Features_scaled['FGM'] * weights['FGM'] +
    df_Features_scaled['STL'] * weights['STL'] +
    df_Features_scaled['PFD'] * weights['PFD'] +
    df_Features_scaled['AST'] * weights['AST']
)

mean = df_Features_scaled['risk_score'].mean()
std = df_Features_scaled['risk_score'].std()




def classify_risk(score):
    if score > mean + (std*2):
        return 'High'
    elif score < mean -(std*2):
        return 'Low'
    else:
        return 'Medium'

df_Features['INJ RISK'] = df_Features_scaled['risk_score'].apply(classify_risk)

####Dashboard Build


#st.title("🏀 NBA Player Injury Risk Dashboard")
st.markdown("<h1 style='text-align: center;'>🏀 NBA Player Injury Risk Dashboard</h1>", unsafe_allow_html=True)
st.markdown("**Data as of Apr 9th, 2024–25 Season**")
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
#filtered_df = df_Features.copy().drop(columns=['risk_score'])

if selected_risk != 'All':
    filtered_df = filtered_df[filtered_df['INJ RISK'] == selected_risk]

if selected_player != 'All':
    filtered_df = filtered_df[filtered_df['PLAYER_NAME'] == selected_player]

if selected_position != 'All':
    filtered_df = filtered_df[filtered_df['POSITION'] == selected_position]

if selected_team != 'All':
    filtered_df = filtered_df[filtered_df['TEAM'] == selected_team]

# Show table

st.dataframe(filtered_df)


# Calculate stats
exp_stats = filtered_df['EXP'].agg(['mean', 'max', 'min'])
fgm_stats = filtered_df['FGM'].agg(['mean', 'max', 'min'])
stl_stats = filtered_df['STL'].agg(['mean', 'max', 'min'])
pfd_stats = filtered_df['PFD'].agg(['mean', 'max', 'min'])
ast_stats = filtered_df['AST'].agg(['mean', 'max', 'min'])

# Format the note with 2 decimal places
note_text = f"""
<small><i>
EXP – mean: {exp_stats['mean']:.2f}, max: {exp_stats['max']:.2f}, min: {exp_stats['min']:.2f}   |  
FGM – mean: {fgm_stats['mean']:.2f}, max: {fgm_stats['max']:.2f}, min: {fgm_stats['min']:.2f}   |  
STL – mean: {stl_stats['mean']:.2f}, max: {stl_stats['max']:.2f}, min: {stl_stats['min']:.2f}   |  
PFD – mean: {pfd_stats['mean']:.2f}, max: {pfd_stats['max']:.2f}, min: {pfd_stats['min']:.2f}   |  
AST – mean: {ast_stats['mean']:.2f}, max: {ast_stats['max']:.2f}, min: {ast_stats['min']:.2f}
</i></small>
"""

# Display note
st.markdown(note_text, unsafe_allow_html=True)
