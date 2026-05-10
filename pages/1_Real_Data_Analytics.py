import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Real Dataset Analytics")
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

    st.markdown("###  Navigation")
# Load dataset
df = pd.read_csv("uber-raw-data-apr14.csv")

# Preprocess
df['Date/Time'] = pd.to_datetime(df['Date/Time'])

df['hour'] = df['Date/Time'].dt.hour
df['weekday'] = df['Date/Time'].dt.weekday

# KPIs
k1, k2, k3 = st.columns(3)

k1.metric("Total Trips", f"{len(df):,}")
k2.metric("Peak Hour", f"{df['hour'].value_counts().idxmax()}:00")
k3.metric("Average Hourly Trips", int(df.groupby('hour').size().mean()))

st.markdown("---")

# Charts
c1, c2 = st.columns(2)

hourly = df['hour'].value_counts().sort_index()

with c1:

    fig1 = px.line(
        x=hourly.index,
        y=hourly.values,
        title="Demand by Hour",
        labels={'x':'Hour','y':'Trips'},
        markers=True
    )

    st.plotly_chart(fig1, use_container_width=True)

weekday_data = df['weekday'].value_counts().sort_index()

weekday_labels = [
    "Mon","Tue","Wed",
    "Thu","Fri","Sat","Sun"
]

with c2:

    fig2 = px.bar(
        x=weekday_labels,
        y=weekday_data.values,
        title="Demand by Weekday"
    )

    st.plotly_chart(fig2, use_container_width=True)

# Heatmap
st.markdown("---")

st.subheader("Pickup Density Heatmap")

selected_hour = st.slider(
    "Select Hour",
    0,
    23,
    12
)

map_df = df[df['hour'] == selected_hour]

if len(map_df) > 5000:
    map_df = map_df.sample(5000)

# FIXED FIG_MAP ERROR
fig_map = px.density_mapbox(
    map_df,
    lat='Lat',
    lon='Lon',
    radius=10,
    zoom=10,
    center=dict(lat=40.75, lon=-73.98),
    mapbox_style="open-street-map",
    title=f"Ride Density at Hour {selected_hour}"
)

st.plotly_chart(fig_map, use_container_width=True)