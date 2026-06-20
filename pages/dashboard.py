import streamlit as st
import pandas as pd
from database.db_connection import get_connection

st.title("📊 Dashboard")

conn = get_connection()

providers = pd.read_sql(
    "SELECT COUNT(*) AS total FROM providers_data",
    conn
).iloc[0, 0]

receivers = pd.read_sql(
    "SELECT COUNT(*) AS total FROM receivers_data",
    conn
).iloc[0, 0]

food = pd.read_sql(
    "SELECT COUNT(*) AS total FROM food_listing_data",
    conn
).iloc[0, 0]

claims = pd.read_sql(
    "SELECT COUNT(*) AS total FROM claims_data",
    conn
).iloc[0, 0]

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Providers", providers)

with col2:
    st.metric("Total Receivers", receivers)

col3, col4 = st.columns(2)

with col3:
    st.metric("Food Listings", food)

with col4:
    st.metric("Total Claims", claims)

conn.close()