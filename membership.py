import streamlit as st
import pandas as pd
firsttable = pd.read_csv("membership.csv")
st.title("Register for Membership")
st.subheader("Personal Info")
name = st.text_input("What is your name: ")
address = st.text_input("What is your address: ")
d1,g2 = st.columns(2)
with d1:
    st.subheader("Day of birth")
    dob1,dob2,dob3 = st.columns(3)
    with dob1:
        Day = st.selectbox("Which day: ",["Choose","Monday","Tuesday","Wednesday","Thursday","Friday","Saturtay","Sunday"])

    with dob2:
        Month = st.selectbox("Which month: ",["Choose","January","Febuary","March","April","May","June","July","August","September","October","November","December"])

    with dob3:
        year = st.selectbox("Which year",["Choose","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023","2024"])
  
    st.subheader("Phone number")
    pn = st.text_input("e",1,label_visibility='collapsed')

with g2:
    st.subheader("Gender")
    gender = st.selectbox("Which gender",["Choose","Boy","Girl"])
    
    st.subheader("Email")
    email = st.text_input("a",label_visibility='collapsed')

st.subheader("Address")
address = st.text_input("Address: ")

st.subheader("Types of membership")
tom1,tom2 = st.columns(2)
with tom1: 
 Tom1 = st.radio("", ["Individual membership","Family membership"])

with tom2:
 Tom2 = st.radio("",["Student membership","Senior citizen membership"])

st.subheader("Emergency Contact Info")
ename = st.text_input("What is your name:")
pn1,emem2 = st.columns(2)
with pn1:
 st.subheader("Phone number")
 epn = st.text_input("y",1,label_visibility='collapsed')
with emem2:
 st.subheader("Email")
 em_mail = st.text_input("t",label_visibility="collapsed")

if st.button("Submit"):
   memberdict = {"Name":[name],"Address":[address],"Phone number":[pn],"Email":[email],"Personal membership":[Tom1],"Work membership":[Tom2],"Emergency name":[ename],"Emergency phone number":[epn],"Emergency email":[em_mail],"Gender":[gender],"Date":[Day],"Month":[Month],"Year":[year]}
   secondtable = pd.DataFrame(memberdict)
   tablesjoin = pd.concat([firsttable,secondtable],ignore_index=True)
   tablesjoin.to_csv("membership.csv",index = False) 