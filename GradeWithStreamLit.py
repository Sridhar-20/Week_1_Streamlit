import streamlit as st
st.title("This is for calculating the grades of a student")

project = st.number_input("Enter the Project Score",min_value=0)
internal = st.number_input("Enter the Internal Score",min_value=0)
external = st.number_input("Enter the External Score",min_value=0)

if st.button("Grade") :
    if project < 50 or internal < 50 or external < 50:
        if project < 50:
            st.write("You are failed in project")
        if internal < 50:
            st.write("You are failed in internal")
        if external < 50:
            st.write("You are failed in external")
    else:
        total = project + internal + external
        pro_per = 0.7 * total
        int_per = 0.1 * total
        ext_per = 0.2 * total
        grade_marks = pro_per + int_per + ext_per
        if grade_marks > 90:
            st.write("A Grade")
        elif grade_marks >= 80:
            st.write("B Grade")
        else:
            st.write("C Grade")