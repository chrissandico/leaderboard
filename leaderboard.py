import streamlit as st
import pandas as pd

# Static leaderboard data
leaderboard_data = {
    "Alice": {"points": 100, "reason": "Excellent homework completion"},
    "Bob": {"points": 85, "reason": "Great class participation"},
    "Charlie": {"points": 95, "reason": "Outstanding project work"},
    "Diana": {"points": 90, "reason": "Consistent effort in all subjects"}
}

def create_dataframe():
    df = pd.DataFrame.from_dict(leaderboard_data, orient='index')
    df['name'] = df.index
    df = df.reset_index(drop=True)
    return df[['name', 'points', 'reason']]

st.title("Weekly Leaderboard")

# Display leaderboard
df = create_dataframe()
st.dataframe(df.sort_values('points', ascending=False))

# Optional: Add some statistics or visualizations
st.subheader("Top Performer")
top_performer = df.loc[df['points'].idxmax()]
st.write(f"**{top_performer['name']}** with {top_performer['points']} points")
st.write(f"Reason: {top_performer['reason']}")

# Optional: Add a bar chart
st.subheader("Points Distribution")
st.bar_chart(df.set_index('name')['points'])