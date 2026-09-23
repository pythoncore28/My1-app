 import streamlit as st

st.title("My First Streamlit App")
st.write("Hello! My Python app is running successfully.")

name = st.text_input("What is your name?")
if st.button("Submit"):
    st.success(f"Welcome, {name}!")
