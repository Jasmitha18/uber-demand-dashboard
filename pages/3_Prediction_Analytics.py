import streamlit as st
import pandas as pd
import plotly.express as px
import os
# ---------------- CUSTOM UI ----------------
st.markdown("""
<style>

/* Main App Background */
.stApp {
    background: linear-gradient(to right, #0f172a, #1e293b);
    color: white;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #111827, #1f2937);
}

/* Sidebar Text */
[data-testid="stSidebar"] * {
    color: white;
}

/* Titles */
h1, h2, h3, h4 {
    color: white !important;
}

/* Metric Cards */
[data-testid="metric-container"] {
    background-color: rgba(255,255,255,0.08);
    border-radius: 15px;
    padding: 15px;
    border: 1px solid rgba(255,255,255,0.1);
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    background-color: #00b894;
    color: white;
    border: none;
    font-size: 16px;
}

/* Dataframes */
[data-testid="stDataFrame"] {
    background-color: rgba(255,255,255,0.05);
    border-radius: 10px;
}

/* Selectbox */
.stSelectbox label {
    color: white !important;
}

/* Slider */
.stSlider label {
    color: white !important;
}

/* Number Input */
.stNumberInput label {
    color: white !important;
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
        "<div class='sidebar-title'>Uber AI Dashboard</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<hr class='sidebar-divider'>",
        unsafe_allow_html=True
    )

    st.markdown("###  Navigation")
st.title("Prediction Analytics")

csv_file = "prediction_history.csv"

if os.path.exists(csv_file):

    df = pd.read_csv(csv_file)

    if not df.empty:

        # KPIs
        k1, k2, k3 = st.columns(3)

        k1.metric(
            "Total Predictions",
            len(df)
        )

        k2.metric(
            "Highest Demand",
            int(df['predicted_demand'].max())
        )

        k3.metric(
            "Average Demand",
            int(df['predicted_demand'].mean())
        )

        st.markdown("---")

        c1, c2 = st.columns(2)

        # Prediction trend
        with c1:

            fig1 = px.line(
                df,
                x=df.index,
                y="predicted_demand",
                markers=True,
                title="Prediction Trend"
            )

            st.plotly_chart(
                fig1,
                use_container_width=True
            )

        # Demand level distribution
        with c2:

            fig2 = px.pie(
                df,
                names="demand_level",
                title="Demand Level Distribution"
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )

        st.markdown("---")

        # Hour-wise prediction chart
        fig3 = px.bar(
            df,
            x="hour",
            y="predicted_demand",
            color="demand_level",
            title="Predicted Demand by Hour"
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

        st.markdown("---")

        st.subheader("Prediction Records")

        st.dataframe(
            df.tail(20),
            use_container_width=True
        )

    else:

        st.warning("Prediction file is empty.")

else:

    st.error("No prediction history found. Generate predictions first.")