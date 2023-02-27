import streamlit as st

# Page title
st.title("EMI Calculator")

# User inputs
principal = st.number_input("Enter the loan amount (in rupees)", step=1)
interest_rate = st.slider("Enter the interest rate (in %)", min_value=6, max_value=15, step=1)
tenure = st.slider("Enter the tenure (in years)", min_value=1, max_value=30, step=1)

# Calculate EMI
interest_rate = interest_rate / (12 * 100)
tenure_months = tenure * 12
emi = int((principal * interest_rate * (1 + interest_rate)**tenure_months) / ((1 + interest_rate)**tenure_months - 1))

# Display EMI
st.write(f"The monthly EMI is {emi:} rupees")
