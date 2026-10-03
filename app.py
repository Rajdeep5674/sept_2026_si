import streamlit as st

st.title("💰 Simple Interest Calculator")

# Input
principal = st.number_input(
    "Please enter principal amount:",
    min_value=0.0,
    step=100.0
)

rate = st.number_input(
    "Please enter rate of interest (%):",
    min_value=0.0,
    step=0.1
)

y = st.number_input(
    "Enter time in year:",
    min_value=0,
    step=1
)

m = st.number_input(
    "Enter time in month:",
    min_value=0,
    max_value=11,
    step=1
)

# Calculate button
if st.button("Calculate Simple Interest"):

    # Convert year + month into total years
    time = y + (m / 12)

    # Simple Interest
    si = (principal * rate * time) / 100

    # Maturity Value
    maturity_value = principal + si

    st.success(f"Your simple interest amount is ₹{si:.2f}")

    st.info(f"Maturity value would be ₹{maturity_value:.2f}")