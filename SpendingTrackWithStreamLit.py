import streamlit as st
st.title("Calculating the percentage of spending")

salary = st.number_input("Enter the salary",min_value=1000.00)
num1 = st.number_input("Enter the shopping bill 1",min_value=1000.00)
num2 = st.number_input("Enter the shopping bill 2",min_value=1000.00)
num3 = st.number_input("Enter the shopping bill 3",min_value=1000.00)

if st.button("Find") :
    total = num1 + num2 + num3
    st.write("The total amount : ", total)

    if salary > 0:  # To avoid division by zero error
        per = (total / salary) * 100
        # Display the percentage
        st.write(f"The percentage of spending compared to your salary: {per:.2f}%")
    else:
        st.write("Please enter a valid salary greater than 0.")
