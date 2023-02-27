import streamlit as st

# Page title
st.title("EMI Calculator")

# User inputs
principal = st.number_input("Enter the loan amount (in rupees)")
interest_rate = st.slider("Enter the interest rate (in %)", min_value=1.0, max_value=15.0, step=0.1)
tenure = st.slider("Enter the tenure (in years)", min_value=1.0, max_value=30.0, step=1.0)

# Calculate EMI
interest_rate = interest_rate / (12 * 100)
tenure_months = tenure * 12
emi = (principal * interest_rate * (1 + interest_rate)**tenure_months) / ((1 + interest_rate)**tenure_months - 1)

# Display EMI
st.write(f"The monthly EMI is {emi:.2f} rupees")