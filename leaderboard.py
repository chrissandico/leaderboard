import streamlit as st
import pandas as pd

# Static leaderboard data
leaderboard_data = {
    "Moses": 2000,
    "Matt": 2000,
    "Seb": 1500,
    "Victoria": 1500,
    "Kingsley": 2000,
    "Cinya": 2000,
    "Sophia": 1500,
    "Preston": 1000,
    "Traie": 1000,
    "Celine": 1000,
    "Izzy": 1000,
    "Lucas": 1000
}

# Points log data (simulating weekly updates)
points_log = [
    {"date": "2024-07-07", "name": "Moses", "points": 1000, "reason": "Knowing core values"},
    {"date": "2024-07-07", "name": "Matt", "points": 1000, "reason": "Demonstrating Teamwork & Inclusion core values"},
    {"date": "2024-07-07", "name": "Seb", "points": 500, "reason": "Duck race winner"},
    {"date": "2024-07-14", "name": "All", "points": 1000, "reason": "Great Demo Day presentation"},
    {"date": "2024-07-14", "name": "Victoria", "points": 500, "reason": "Duck race winner"},
    {"date": "2024-07-21", "name": "Kingsley", "points": 1000, "reason": "Demonstrating Teamwork core value"},
    {"date": "2024-07-21", "name": "Cinya", "points": 1000, "reason": "Demonstrating Fun core value"},
    {"date": "2024-07-21", "name": "Sophia", "points": 500, "reason": "Duck race winner"}
]

def create_dataframe():
    df = pd.DataFrame.from_dict(leaderboard_data, orient='index', columns=['points'])
    df['name'] = df.index
    df = df.reset_index(drop=True)
    return df[['name', 'points']]

st.title("Core Values Leaderboard")

# Display leaderboard
df = create_dataframe()
st.dataframe(df.sort_values('points', ascending=False))

# Points Log Table
st.subheader("Points Log")
log_df = pd.DataFrame(points_log)
log_df['date'] = pd.to_datetime(log_df['date'])
log_df = log_df.sort_values('date', ascending=False)
st.table(log_df)

# Points Distribution Bar Chart
st.subheader("Points Distribution")
st.bar_chart(df.set_index('name')['points'])

