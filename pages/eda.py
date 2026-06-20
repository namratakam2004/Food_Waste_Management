import streamlit as st
import pandas as pd
import plotly.express as px
from database.db_connection import get_connection

st.title("📈 EDA Dashboard")

conn = get_connection()

food_df = pd.read_sql(
    "SELECT * FROM food_listing_data",
    conn
)

claims_df = pd.read_sql(
    "SELECT * FROM claims_data",
    conn
)

# Food Type Distribution
food_type_count = (
    food_df["food_type"]
    .value_counts()
    .reset_index()
)

food_type_count.columns = [
    "Food Type",
    "Count"
]

fig1 = px.bar(
    food_type_count,
    x="Food Type",
    y="Count",
    title="Food Type Distribution"
)

st.plotly_chart(fig1)

# Meal Type Distribution
meal_type_count = (
    food_df["meal_type"]
    .value_counts()
    .reset_index()
)

meal_type_count.columns = [
    "Meal Type",
    "Count"
]

fig2 = px.bar(
    meal_type_count,
    x="Meal Type",
    y="Count",
    title="Meal Type Distribution"
)

st.plotly_chart(fig2)

# Claim Status Distribution
status_count = (
    claims_df["status"]
    .value_counts()
    .reset_index()
)

status_count.columns = [
    "Status",
    "Count"
]

fig3 = px.pie(
    status_count,
    names="Status",
    values="Count",
    title="Claim Status Distribution"
)

st.plotly_chart(fig3)

conn.close()