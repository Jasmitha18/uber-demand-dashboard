import streamlit as st

st.set_page_config(
    page_title="Uber Demand Dashboard",
    page_icon="",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #141e30 0%, #243b55 100%);
}

/* Sidebar text */
[data-testid="stSidebar"] * {
    color: white;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    border-radius: 18px;
    padding: 25px;
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.15);
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.15);
}

/* Auto-adjust text color */
.card h2 {
    color: inherit;
    font-weight: 700;
}

/* Buttons */
.stButton > button {
    width: 100%;
    height: 3em;
    border-radius: 12px;
    font-weight: 600;
    font-size: 15px;
}

/* Metric Cards */
[data-testid="metric-container"] {
    background: rgba(128,128,128,0.08);
    border: 1px solid rgba(128,128,128,0.20);
    padding: 15px;
    border-radius: 15px;
}

/* Tables */
[data-testid="stDataFrame"] {
    border-radius: 10px;
}

/* Charts */
.js-plotly-plot {
    border-radius: 12px;
}

/* Tabs */
.stTabs [data-baseweb="tab"] {
    font-size: 16px;
    font-weight: 600;
}

/* Headers */
h1, h2, h3 {
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🚖 Uber Demand Dashboard")
st.markdown("---")

# ---------------- ROW 1 ----------------
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h2>📊 Real Data Analytics</h2>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Analytics"):
        st.switch_page("pages/1_Real_Data_Analytics.py")

with col2:
    st.markdown("""
    <div class="card">
        <h2>🤖 Demand Prediction</h2>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Prediction"):
        st.switch_page("pages/2_Demand_Prediction.py")

# ---------------- ROW 2 ----------------
col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="card">
        <h2>📈 Prediction Analytics</h2>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Prediction Analytics"):
        st.switch_page("pages/3_Prediction_Analytics.py")

with col4:
    st.markdown("""
    <div class="card">
        <h2>Prediction Dataset</h2>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Dataset"):
        st.switch_page("pages/4_Prediction_Dataset.py")