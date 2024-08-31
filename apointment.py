import streamlit as st
st.title("Doctor Appointment Request Form")
st.write("Fill the form below and we will get back  soon to you for more updates and plan your appointment.")
st.subheader("Name")
n1,n2 = st.columns(2)
with n1:
    fn = st.text_input("First name: ")

with n2:
    ln = st.text_input("Last name: ")

st.subheader("Date of birth")
dob1,dob2,dob3 = st.columns(3)
with dob1:
    day = st.selectbox("Please select a Day",["Choose","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])

with dob2:
    month = st.selectbox("Please select a Month",["Choose","January","Febuary","March","April","May","June","July","August","September","October","November","December"])

with dob3:
    year = st.selectbox("Please select a year",["Choose","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023","2024"])

g1,pn2 = st.columns(2)
with g1:
    st.subheader("Gender")
    g1 = st.selectbox("Please select ",["Choose","Boy","Girl"])

with pn2:
    st.subheader("Phone number")
    pn1 = st.number_input(" ",1)

st.write("**Address**")
address = st.text_input("Street address: ")
address2 = st.text_input("Street Address line 2: ")

c1,sp2 = st.columns(2)
with c1:
    city = st.text_input("City: ")

with sp2:
    state = st.text_input("State/Provice: ")

vip = st.text_input("Postal/vip code: ")

st.write("**Email**")
email = st.text_input("Enter your email: ")

applied = st.selectbox("Have you ever applied to our facility before",["None","Yes","No"])

department = st.text_input("Which department would you like an appointment from?: ")

procedure = st.selectbox("Which procedure do you want to make an appointment for?",["None","Xray","Test","Child birth","Surgury"])

st.write("Preferred Appointed Date")

if st.button("Submit"):
    st.success("Submitted")
