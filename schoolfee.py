"""
# create a simple page for a school. 
# Show on the page the Elementary fee is 300,000 naira and the college fee is 500,000 naira
# Ask the parent name
# Ask how many kids the parent have for elementary and ask if how many they have for college
# Then show them their total tuition fee
"""
import streamlit as st
elementaryfe = 300000
collegefe = 500000
st.write(f"The Elementaryfees is {elementaryfe} and the Collegefees is {collegefe}")
parents = st.text_input("What is the parents name:")
phone = st.text_input("Whats your phone number:")

kids1,kids2 = st.columns(2)
with kids1:
    elementarykids = st.number_input("How many elemetary kids do you have: ",0)
    elementaryfee = elementarykids *elementaryfe

with kids2:
    collegekids = st.number_input("How many college kids do you have: ",0)
    collegefee = collegekids * collegefe

totalfee = elementaryfee+collegefee
if st.button("How much school fees"):
    st.write(f"the Total fee is {totalfee}")    