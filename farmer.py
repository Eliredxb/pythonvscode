"""
JULY 11, 2024
A farmer starts with a herd of 50 animals. Over time, various events cause the farmer to lose some of these animals. The farmer decides to keep track of the losses to determine how many animals are left at the end of the period. Here’s how the farmer does it:

The farmer initially has 50 animals.
The farmer sells some animals at the market.
Some animals are eaten by predators.
Some animals die from disease.
Some animals are stolen.
Start by defining the initial number of animals as initial_animals and set it to 50.
Ask the farmer how many animals were sold and store it in a variable called sold_animals (as an integer).
Ask the farmer how many animals were eaten by predators and store it in a variable called eaten_by_predators (as an integer).
Ask the farmer how many animals died from disease and store it in a variable called died_from_disease (as an integer).
Ask the farmer how many animals were stolen and store it in a variable called stolen_animals (as an integer).
Calculate the total number of animals lost by adding sold_animals, eaten_by_predators, died_from_disease, and stolen_animals.
Subtract the total number of animals lost from initial_animals to get the remaining number of animals.
Use an if condition to check if the remaining number of animals is still positive or if the farmer has lost more animals than they initially had.
Print a message that tells the farmer how many animals are left and whether they have any animals left or if they have lost more than they initially had.
PYTHON BLOCKS
"""
import streamlit as st
initial_animals = 50
sold_animals = st.number_input("How many animals where sold: ",0,50)
eaten_by_predators = st.number_input("How many animals were eaten by preditors: ",0,50)
died_from_disease = st.number_input("How many animals died from disease: ",0,50)
stolen_animals = st.number_input("How many animals have been stolen",0 ,50)
total_loss = stolen_animals+died_from_disease+eaten_by_predators+sold_animals
total_animals = initial_animals - total_loss
if st.button("Do i remain"):
  if total_animals == 50:
      st.success("No You remained with the amount you started with")

  else:
      st.error("Yes You got lower than you initial")

