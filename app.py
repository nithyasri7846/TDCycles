import streamlit as st
import math

# Page config
st.set_page_config(page_title="Thermodynamic Cycles Calculator", layout="centered")

# Custom CSS Styling
st.markdown("""
    <style>
        .stApp {
            background-color: black;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2 {
            color: #003366;
            text-align: center;
        }
        .sidebar .sidebar-content {
            background-color: #e6f0ff;
        }
        .stButton>button {
            background-color: #007acc;
            color: white;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #005f99;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("Thermodynamic Cycles Calculator")

# Sidebar Selection
cycle = st.sidebar.selectbox(
    "Select Thermodynamic Cycle",
    ("Otto Cycle", "Diesel Cycle", "Dual Cycle")
)

# Otto Cycle
if cycle == "Otto Cycle":
    st.header("Otto Cycle")
    r = st.number_input("Compression Ratio (r)", min_value=1.1, value=8.0)
    gamma = st.number_input("γ (specific heat ratio)", min_value=1.0, value=1.4)
    T1 = st.number_input("Initial Temperature T1 (K)", min_value=200.0, value=300.0)
    p1 = st.number_input("Initial Pressure p1 (Pa)", min_value=10000.0, value=101325.0)

    if st.button("Calculate Otto Cycle"):
        T2 = T1 * (r ** (gamma - 1))
        T3 = T2 + 500  # Assumed heat addition
        T4 = T3 * (1 / r) ** (gamma - 1)
        efficiency = 1 - (1 / (r ** (gamma - 1)))

        st.success(f"T2 = {T2:.2f} K")
        st.success(f"T3 = {T3:.2f} K")
        st.success(f"T4 = {T4:.2f} K")
        st.success(f"Efficiency = {efficiency * 100:.2f} %")

# Diesel Cycle
elif cycle == "Diesel Cycle":
    st.header("Diesel Cycle")
    r = st.number_input("Compression Ratio (r)", min_value=1.1, value=18.0)
    rc = st.number_input("Cut-off Ratio (rc)", min_value=1.0, value=2.0)
    gamma = st.number_input("γ (specific heat ratio)", min_value=1.0, value=1.4)
    T1 = st.number_input("Initial Temperature T1 (K)", min_value=200.0, value=300.0)

    if st.button("Calculate Diesel Cycle"):
        T2 = T1 * (r ** (gamma - 1))
        T3 = T2 * rc
        T4 = T3 * ((1 / r) ** (gamma - 1)) * ((rc - 1) / rc)
        efficiency = 1 - ((1 / (r ** (gamma - 1))) * ((rc ** gamma - 1) / (gamma * (rc - 1))))

        st.success(f"T2 = {T2:.2f} K")
        st.success(f"T3 = {T3:.2f} K")
        st.success(f"T4 = {T4:.2f} K")
        st.success(f"Efficiency = {efficiency * 100:.2f} %")

# Dual Cycle
elif cycle == "Dual Cycle":
    st.header("Dual Cycle")
    r = st.number_input("Compression Ratio (r)", min_value=1.1, value=16.0)
    rc = st.number_input("Cut-off Ratio (rc)", min_value=1.0, value=2.0)
    rp = st.number_input("Constant Volume Ratio (rp)", min_value=1.0, value=1.5)
    gamma = st.number_input("γ (specific heat ratio)", min_value=1.0, value=1.4)
    T1 = st.number_input("Initial Temperature T1 (K)", min_value=200.0, value=300.0)

    if st.button("Calculate Dual Cycle"):
        T2 = T1 * (r ** (gamma - 1))
        T3 = T2 * rp
        T4 = T3 * rc
        T5 = T4 * ((1 / r) ** (gamma - 1))

        efficiency = 1 - (
            1 / (r ** (gamma - 1)) *
            ((rp * rc) ** gamma - 1) /
            (gamma * (rp - 1 + gamma * rc))
        )

        st.success(f"T2 = {T2:.2f} K")
        st.success(f"T3 = {T3:.2f} K")
        st.success(f"T4 = {T4:.2f} K")
        st.success(f"T5 = {T5:.2f} K")
        st.success(f"Efficiency = {efficiency * 100:.2f} %")
