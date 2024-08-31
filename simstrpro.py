import streamlit as st
st.title("ATM")
money = 1000
st.subheader(f"${money}")
    #if st.sidebar.button("Withdraw"):
amount = st.number_input("Input amount: ",0)
b1,b2 = st.columns(2)


with b1:
    wbut = st.button("Withdraw")
    if wbut:
        money = money - amount
        st.success(f"You have successfully withdraw ${amount}")
        st.write(f"Your new balance is ${money}")

with b2:
    dbut = st.button("Deposit")
    if dbut:
        money = money + amount
        st.success(f"You have successfully deposited ${amount}")
        st.write(f"Your new balance is ${money}")