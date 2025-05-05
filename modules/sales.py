
import streamlit as st

def render(df):
    st.subheader("💼 Sales Dashboard")
    st.metric("Total Sales", df[df.columns[1]].sum())
    st.metric("Monthly Growth", "12.5%")
