import streamlit as st

st.set_page_config(
    page_title="Uber Demand Dashboard",
    page_icon="🚖",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #141e30, #243b55);
}

[data-testid="stSidebar"] * {
    color: white;
}

.main {
    background-color: #0e1117;
    color: white;
}

.card {
    background-color: #1f2937;
    padding: 30px;
    border-radius: 18px;
    text-align: center;
    margin-bottom: 25px;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.3);
}

.card h2 {
    color: white;
}

.stButton>button {
    width: 100%;
    height: 3em;
    border-radius: 10px;
    background-color: #00b894;
    color: white;
    font-size: 16px;
    border: none;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title(" Uber Demand Dashboard")

st.markdown("---")

# ---------------- ROW 1 ----------------
col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="card">
        <h2>Real Data Analytics</h2>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Analytics"):

        st.switch_page("pages/1_Real_Data_Analytics.py")

with col2:

    st.markdown("""
    <div class="card">
        <h2>Demand Prediction</h2>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Prediction"):

        st.switch_page("pages/2_Demand_Prediction.py")

# ---------------- ROW 2 ----------------
col3, col4 = st.columns(2)

with col3:

    st.markdown("""
    <div class="card">
        <h2> Prediction Analytics</h2>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Prediction Analytics"):

        st.switch_page("pages/3_Prediction_Analytics.py")

with col4:

    st.markdown("""
    <div class="card">
        <h2> Prediction Dataset</h2>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Dataset"):

        st.switch_page("pages/4_Prediction_Dataset.py")