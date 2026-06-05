import streamlit as st
import pandas as pd
import os

st.title("Prediction Dataset")
# ---------------- MODERN UI ----------------
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    color: white;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: rgba(17, 25, 40, 0.75);
    backdrop-filter: blur(16px);
    border-right: 1px solid rgba(255,255,255,0.1);
}

/* Sidebar Text */
[data-testid="stSidebar"] * {
    color: white;
}

/* Main Titles */
h1 {
    color: #ffffff;
    font-size: 42px !important;
    font-weight: bold;
}

h2, h3, h4 {
    color: #e2e8f0;
}

/* Metric Cards */
[data-testid="metric-container"] {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.12);
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 0px 20px rgba(128,0,255,0.25);
}

/* Buttons */
.stButton > button {
    background: linear-gradient(to right, #7f00ff, #e100ff);
    color: white;
    border: none;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.03);
    box-shadow: 0px 0px 20px rgba(225,0,255,0.6);
}

/* Input Fields */
.stSelectbox div,
.stNumberInput div,
.stTextInput div {
    border-radius: 12px !important;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    border-radius: 15px;
    overflow: hidden;
}

/* Charts */
.js-plotly-plot {
    border-radius: 20px;
    overflow: hidden;
    background: rgba(255,255,255,0.04);
    padding: 10px;
}

/* Slider */
.stSlider label {
    color: white !important;
}

/* Labels */
label {
    color: #f8fafc !important;
    font-weight: 500;
}

</style>
""", unsafe_allow_html=True)
# ---------------- ADVANCED SIDEBAR UI ----------------
st.markdown("""
<style>

/* Main App */
.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    color: white;
}

/* SIDEBAR */
[data-testid="stSidebar"] {

    background: rgba(15, 23, 42, 0.75);

    backdrop-filter: blur(18px);

    border-right: 1px solid rgba(255,255,255,0.08);

    box-shadow: 0 0 25px rgba(128,0,255,0.3);
}

/* Sidebar Content */
[data-testid="stSidebar"] * {
    color: white;
}

/* Sidebar Navigation Buttons */
section[data-testid="stSidebar"] .stButton > button {

    background: rgba(255,255,255,0.08);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 14px;

    height: 3em;

    margin-bottom: 10px;

    font-size: 15px;

    font-weight: 500;

    transition: 0.3s;
}

/* Hover Effect */
section[data-testid="stSidebar"] .stButton > button:hover {

    background: linear-gradient(to right, #7f00ff, #e100ff);

    transform: translateX(5px);

    box-shadow: 0px 0px 20px rgba(225,0,255,0.5);
}

/* Sidebar Header */
.sidebar-title {

    font-size: 28px;

    font-weight: bold;

    text-align: center;

    margin-top: 10px;

    margin-bottom: 25px;

    color: white;

    text-shadow: 0px 0px 10px rgba(255,255,255,0.5);
}

/* Sidebar Divider */
.sidebar-divider {

    border: 1px solid rgba(255,255,255,0.08);

    margin-top: 10px;

    margin-bottom: 20px;
}

/* Metrics */
[data-testid="metric-container"] {

    background: rgba(255,255,255,0.08);

    border-radius: 18px;

    padding: 15px;

    backdrop-filter: blur(12px);

    border: 1px solid rgba(255,255,255,0.08);
}

/* Buttons Main */
.stButton > button {

    background: linear-gradient(to right, #7f00ff, #e100ff);

    color: white;

    border: none;

    border-radius: 12px;

    height: 3em;

    font-size: 16px;

    font-weight: bold;
}

/* Titles */
h1, h2, h3 {

    color: white;
}

</style>
""", unsafe_allow_html=True)
with st.sidebar:

    st.markdown(
        "<div class='sidebar-title'> Uber AI Dashboard</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<hr class='sidebar-divider'>",
        unsafe_allow_html=True
    )

    st.markdown("### Navigation")

csv_file = "prediction_history.csv"

if os.path.exists(csv_file):

    df = pd.read_csv(csv_file)

    st.subheader("Stored Prediction Dataset")

    # KPIs
    k1, k2, k3 = st.columns(3)

    k1.metric("Rows", df.shape[0])

    k2.metric("Columns", df.shape[1])

    k3.metric(
        "Average Prediction",
        int(df['predicted_demand'].mean())
    )

    st.markdown("---")

    st.dataframe(
        df,
        use_container_width=True
    )

else:

    st.warning("No stored prediction dataset found.")