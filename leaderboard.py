import streamlit as st
import pandas as pd

# Static leaderboard data
leaderboard_data = {
    "Moses": 2000,
    "Matt": 2000,
    "Seb": 2000,
    "Victoria": 1500,
    "Kingsley": 2000,
    "Cinya": 2000,
    "Sophia": 2500,
    "Preston": 1000,
    "Traie": 2000,
    "Celine": 1000,
    "Izzy": 1000,
    "Lucas": 1000
}

# Points log data (simulating weekly updates)
points_log = [
    {"date": "2024-07-07", "name": "Moses", "bucks": 1000, "reason": "Knowing core values"},
    {"date": "2024-07-07", "name": "Matt", "bucks": 1000, "reason": "Demonstrating Teamwork & Inclusion core values"},
    {"date": "2024-07-07", "name": "Seb", "bucks": 500, "reason": "Duck race winner"},
    {"date": "2024-07-14", "name": "All", "bucks": 1000, "reason": "Great Demo Day presentation"},
    {"date": "2024-07-14", "name": "Victoria", "bucks": 500, "reason": "Duck race winner"},
    {"date": "2024-07-21", "name": "Kingsley", "bucks": 1000, "reason": "Demonstrating Teamwork core value"},
    {"date": "2024-07-21", "name": "Cinya", "bucks": 1000, "reason": "Demonstrating Fun core value"},
    {"date": "2024-07-21", "name": "Sophia", "bucks": 500, "reason": "Duck race winner"},
    {"date": "2024-07-28", "name": "Traie", "bucks": 1000, "reason": "Demonstrating Innovation core value"},
    {"date": "2024-07-28", "name": "Sophia", "bucks": 1000, "reason": "Demonstrating Discovery core value"},
    {"date": "2024-07-28", "name": "Seb", "bucks": 500, "reason": "Duck race winner"}
]

def create_dataframe():
    df = pd.DataFrame.from_dict(leaderboard_data, orient='index', columns=['bucks'])
    df['name'] = df.index
    df = df.reset_index(drop=True)
    return df[['name', 'bucks']]

st.title("Core Values Tracker")

# Display leaderboard
df = create_dataframe()
st.dataframe(df.sort_values('bucks', ascending=False))

# Points Log Table
st.subheader("Log")
log_df = pd.DataFrame(points_log)
log_df['date'] = pd.to_datetime(log_df['date'])
log_df = log_df.sort_values('date', ascending=False)
st.table(log_df)

# Points Distribution Bar Chart
st.subheader("Distribution")
st.bar_chart(df.set_index('name')['bucks'])

