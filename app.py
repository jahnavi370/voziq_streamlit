import streamlit as st
from cal import sum, sub, mul, div, mod

st.write("App for cal")
st.header("Cal")

a = st.number_input("Enter first number : ")
b = st.number_input("Enter second number : ")

operator = st.selectbox("Operator",['+','-','*','/','%'])

submit = st.button("Answer")

st.write(submit)

if(submit):
    if operator == '+':
        ans = sum(a,b)
    elif operator == '-':
        ans = sub(a,b)
    elif operator == '*':
        ans = mul(a,b)
    elif operator == '/':
        ans = div(a,b)
    elif operator == '%':
        ans = mod(a,b)
    elif operator == '**':
        ans = pow(a,b)

    st.write(f"The answer is : {ans}")