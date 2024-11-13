"""
A family is planning a camping trip and needs to pack essential items. They start with an empty list and add items as they think of what they need for the trip.

Write a Python program to help them create a packing list.

Start by defining an empty list called packing_list.
Ask each family member to input an item they think is essential for the trip.
Add each item to the packing_list.
After each addition, use an if condition to check:
If the list already has more than 15 items, print a message suggesting they may be overpacking.
If the list already contains the item (i.e., a duplicate item), print a message that the item is already packed.
Once everyone has finished adding items, print the complete packing_list to review what’s been packed.
"""
import streamlit as st

packing_list = []
asking = st.multiselect("What do you want to pack: ",["Tent","Log","Charcoal","Flashlight","Snack","Pillow","Lighter"])
if "Tent" in asking:
  packing_list.append('Tent')
  st.success("Packed")

if "Log" in asking:
    packing_list.append("Log")
    st.success("Packed")

if  "Charcoal" in asking:
    packing_list.append("Charcoal")    
    st.success("Packed")

if  "Flashlight" in asking:
    packing_list.append('Flashlight')
    st.success("Packed")

if  "Snack" in asking:
    packing_list.append('Snack')
    st.success("Packed")

if  "Pillow" in asking:
    packing_list.append('Pillow')
    st.success("Packed")

if  "Lighter" in asking:
    packing_list.append('Lighter')
    st.success("Packed")


st.write("This is what you packed",packing_list) 

   