"""
Liam is an enthusiastic football fan and wants to enhance his game-day experience by purchasing various items. He plans to buy match tickets, a season pass, team merchandise, snacks, and even subscribe to a premium sports channel. Write a Python program to help Liam calculate the total cost of his football adventure.

Liam’s journey through the football shopping spree involves several steps:

Match Ticket Purchase:

Liam needs to purchase match tickets, which cost $100 each.
Account Login:

Liam will log in to his account using his username and password.
Season Pass Selection:

Liam can choose one of the following season passes:
Standard Pass for $200
VIP Pass for $500
Team Merchandise:

Liam can browse through various team merchandise:
Jersey for $60
Scarf for $30
Hat for $20
Snacks Purchase:

Liam can buy snacks for the match:
Popcorn for $10
Hotdog for $15
Soda for $5
Premium Sports Channel Subscription:

Liam can subscribe to a premium sports channel:
Monthly subscription for $20
Annual subscriptionp for $200
Total Calculation:
S
After making his selections, Liam wants to see the total cost of his football adventure.
"""
import streamlit as st
total =  0
st.title("Match ticket purchase")
tickets = st.selectbox("Do you want tickets",["Choose","Yes","No"])
if tickets == "Yes":
    total += 100
st.title("Login")
username = st.text_input("What is your username: ")
password = st.text_input("What is your password: ",type = "password")
st.title("Season pass section")
passes = st.selectbox("Which pass do you want",["Choose","Standard Pass","VIP Pass"]) 
if passes == "Standard Pass":
    total += 200
elif passes == "VIP Pass":
    total += 500
st.title("Team Merchandise")        
merch = st.selectbox("Which merch do you want",["Choose","Jersey","Scarf","Hat"])
if merch == "Jersey":
    total += 60
elif merch == "Scarf":
    total += 30
elif merch == "Hat":
    total += 20
st.title("Snacks")
snacks = st.selectbox("Choose a snack",["Choose","Popcorn","Hotdog","Soda"])
if snacks == "Popcorn":
    total += 10 
elif snacks == "Hotdog":
    total += 15
elif snacks == "Soda":
    total += 5          

st.title("Premium Sports Channel Subscription")
sub = st.selectbox("Which one will you choose",["Choose","Monthly subcription","Annual subscription"])
if sub == "Monthly subscription":
    total += 20
elif sub == "Annuallsubscription":
    total += 200

st.title("Total Calculation")
if st.button("Total"):
    st.write(F"YOU MUST PAY ${total}")