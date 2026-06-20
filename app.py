import streamlit as st

st.set_page_config(
    page_title="Food Waste Management System",
    page_icon="🍲",
    layout="wide"
)

st.title("🍲 Food Waste Management System")

st.write("""
Welcome to the Food Waste Management System.

Use the sidebar to navigate between:
- Dashboard
- Food Listings
- SQL Analysis
- EDA
- CRUD Operations
""")