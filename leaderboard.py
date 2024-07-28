import streamlit as st
import pandas as pd

# Static leaderboard data
leaderboard_data = {
    "Alice": 100,
    "Bob": 85,
    "Charlie": 95,
    "Diana": 90
}

# Points log data (simulating weekly updates)
points_log = [
    {"date": "2024-07-21", "name": "Alice", "points": 20, "reason": "Perfect attendance"},
    {"date": "2024-07-21", "name": "Bob", "points": 15, "reason": "Helping classmates"},
    {"date": "2024-07-14", "name": "Charlie", "points": 25, "reason": "Winning science fair"},
    {"date": "2024-07-14", "name": "Diana", "points": 10, "reason": "Improved test scores"},
    {"date": "2024-07-07", "name": "Alice", "points": 30, "reason": "Outstanding presentation"},
    {"date": "2024-07-07", "name": "Bob", "points": 20, "reason": "Volunteer work"}
]

def create_dataframe():
    df = pd.DataFrame.from_dict(leaderboard_data, orient='index', columns=['points'])
    df['name'] = df.index
    df = df.reset_index(drop=True)
    return df[['name', 'points']]

st.title("Weekly Leaderboard")

# Display leaderboard
df = create_dataframe()
st.dataframe(df.sort_values('points', ascending=False))

# Points Distribution Bar Chart
st.subheader("Points Distribution")
st.bar_chart(df.set_index('name')['points'])

# Points Log Table
st.subheader("Points Log")
log_df = pd.DataFrame(points_log)
log_df['date'] = pd.to_datetime(log_df['date'])
log_df = log_df.sort_values('date', ascending=False)
st.table(log_df)