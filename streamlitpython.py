import streamlit as st

number1 = st.number_input("Insert a number", key="number1")
number2 = st.number_input("Insert a number", key="number2")

# Create the selectbox for choosing the operation symbol
option = st.selectbox(
    "Choose the symbol",
    ("+", "-", "*", "/", "%")
)

st.write(number1, option, number2)

if st.button('Calculate'):
    if option == "+":
        result = number1 + number2
    elif option == "-":
        result = number1 - number2
    elif option == "*":
        result = number1 * number2
    elif option == "/":
        if number2 != 0:
            result = number1 / number2
        else:
            result = "Division by zero is not allowed"
    elif option == "%":
        if number2 != 0:
            result = number1 % number2
        else:
            result = "Division by zero is not allowed"
    
    st.write("Result:", result)

