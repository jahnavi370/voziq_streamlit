import streamlit as st

p = st.number_input("Enter Amount : ")
t = st.number_input("Enter Tenure : ")
r = st.number_inputt("Enter rate of intrest")

st.write((p*t*r)/100)