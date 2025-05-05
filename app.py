
import streamlit as st
import utils.data_loader as data_loader
import utils.forecasting as forecasting
import utils.anomaly_detection as anomaly_detection
import utils.llm_insights as llm_insights
import modules.cybersecurity as cybersecurity
import modules.sales as sales

# Public sharing (ngrok) removed for GitHub demo simplicity

# Mocked LLM for public demo
def MockLLM():
    class Dummy:
        def __call__(self, prompt):
            return "This is a mock AI-generated summary for demonstration purposes."
    return Dummy()

# Custom branding and dark theme layout
st.set_page_config(
    page_title="Intelligence Dashboard Demo",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    body {
        background-color: #0e1117;
        color: #fafafa;
    }
    .main .block-container {
        padding-top: 2rem;
    }
    h1, h2, h3, h4 {
        color: #00ffcc;
    }
</style>
""", unsafe_allow_html=True)

st.title(" Intelligence Metrics Dashboard")

uploaded_file = st.sidebar.file_uploader("Upload CSV or Log File", type=["csv", "log"])
module = st.sidebar.selectbox("Select Module", ["Cybersecurity", "Sales"])

if uploaded_file:
    df = data_loader.load_data(uploaded_file)

    if module == "Cybersecurity":
        cybersecurity.render(df, subdomain="General")  # Hardcoded for demo
    else:
        sales.render(df)

    forecast_fig = forecasting.plot_forecast(df)
    st.plotly_chart(forecast_fig)

    anomalies_fig = anomaly_detection.plot_anomalies(df)
    st.plotly_chart(anomalies_fig)

    llm = MockLLM()
    insights = llm_insights.generate_summary(df, llm)
    st.markdown(f"###  AI Executive Summary\n{insights}")

    if st.button("📧 Send PDF Report"):
        st.info("Email sending is disabled in this public demo.")
else:
    st.info("Upload a file to get started.")
