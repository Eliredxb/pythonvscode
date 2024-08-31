import streamlit as st
st.title("Register for Membership")
st.subheader("Personal Info")
name = st.text_input("What is your name: ")
address = st.text_input("What is your address: ")
st.subheader("Day of birth")

dob1,dob2,dob3 = st.columns(3)
with dob1:
    Day = st.selectbox("Which day: ",["Choose","Monday","Tuesday","Wednesday","Thursday","Friday","Saturtay","Sunday"])

with dob2:
    Month = st.selectbox("Which month: ",["Choose","January","Febuary","March","April","May","June","July","August","September","October","November","December"])

with dob3:
    year = st.selectbox("Which year",["Choose","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023","2024"])


st.subheader("Gender")
gender = st.selectbox("Which gender",["Choose","Boy","Girl"])

st.subheader("Phone number")
pn = st.number_input(" ",1)

st.subheader("Email")
email = st.text_input("What is your email: ")

st.subheader("Address")
address = st.text_input("Address: ")

st.subheader("Types of membership")
st.radio("",["individual membership","Family membership","Student membership","Senior citizen membership"])

st.subheader("Emergency Contact Info")
ename = st.text_input("What is your name: ")
epn = st.number_input(" ",1)
em = email = st.text_input("What is your email: ")

st.subheader("Optional")
Optional = st.number_input("Pls donate: ",1)