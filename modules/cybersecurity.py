
import streamlit as st

def render(df, subdomain):
    st.subheader(f"🔐 Cybersecurity Dashboard - {subdomain}")
    st.metric("Attack Frequency", df.shape[0])
    st.metric("Mean Time to Respond", "3.2 hrs")
