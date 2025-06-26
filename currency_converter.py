import streamlit as st
import requests as req

st.title("Live Currency Converter")

amount = st.number_input("Enter amout in INR", min_value=1)
target = st.selectbox("Select currenct", ["USD", "EUR", "GBP", "JPY", "AUD"])

if st.button("Convert"):
    url = f"https://api.exchangerate-api.com/v4/latest/INR"
    response = req.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][target]
        converted = rate * amount
        st.success(f"{amount} INR = {converted} {target}")
    else:
        st.error("Failed to fetch exchange rates. Please try again later.")