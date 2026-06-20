import streamlit as st
import pandas as pd
from database.db_connection import get_connection

st.title("🍲 Food Listings")

conn = get_connection()

query = """
SELECT *
FROM food_listing_data
"""

df = pd.read_sql(query, conn)

# Filters
city = st.selectbox(
    "Select City",
    ["All"] + sorted(df["location"].unique().tolist())
)

food_type = st.selectbox(
    "Select Food Type",
    ["All"] + sorted(df["food_type"].unique().tolist())
)

meal_type = st.selectbox(
    "Select Meal Type",
    ["All"] + sorted(df["meal_type"].unique().tolist())
)

provider_type = st.selectbox(
    "Select Provider Type",
    ["All"] + sorted(df["provider_type"].unique().tolist())
)

filtered_df = df.copy()

if city != "All":
    filtered_df = filtered_df[
        filtered_df["location"] == city
    ]

if food_type != "All":
    filtered_df = filtered_df[
        filtered_df["food_type"] == food_type
    ]

if meal_type != "All":
    filtered_df = filtered_df[
        filtered_df["meal_type"] == meal_type
    ]

if provider_type != "All":
    filtered_df = filtered_df[
        filtered_df["provider_type"] == provider_type
    ]

st.subheader("Available Food Listings")

st.dataframe(
    filtered_df,
    use_container_width=True
)

conn.close()