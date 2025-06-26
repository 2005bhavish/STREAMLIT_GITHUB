import streamlit as st
import datetime
st.title("--------AGE CALCULATOR-----------------")

dob = st.date_input("Enter your date of birth")
if dob:
    today = datetime.now().date()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    st.success(f"Your age is: {age} years")