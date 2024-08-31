"""
Write a Python program for students to check their scholarship eligibility. Create a menu for the "Check Scholarship" page and the "Scholarship Database" page.
Ask for the student's name.
Ask for their GPA.
Based on their GPA, determine what type of scholarship they are eligible for:
If their GPA is below 2.5, they are not eligible for a scholarship.
If their GPA is between 2.5-3.0, they are eligible for a partial scholarship.
If their GPA is between 3.0-3.5, they are eligible for a half scholarship.
If their GPA is between 3.5-4.0, they are eligible for a full scholarship.
Implement the program so that it displays the appropriate message to the student based on their GPA.
"""
import streamlit as st
st.set_page_config(layout ="wide")
name = st.text_input("What is the students name: ")
gpa = st.selectbox("Whats your GPA: ",[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4.0])

if gpa < 2.5:
    st.error(f"{name} you are not eligible for a scholarship.")
elif gpa >= 2.5 and gpa < 3.0:
    st.warning(f"{name}y ou are  eligible for a partial scholarship.")
elif gpa >= 3.0 and gpa <= 3.5:
    st.info(f"{name} you are eligible for a half scholarship") 
elif gpa >= 3.5 and gpa <= 4.0:
    st.success(f"{name} you are eligible for a full scholarship")
    st.balloons()
