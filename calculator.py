import streamlit as st

st.title("🧮 Simple Expression Calculator")

expression = st.text_input('Enter the expression (e.g., 2+3*5):')

if st.button('Evaluate'):
    try:
        result = eval(expression)
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Invalid expression ❌\nError: {e}")