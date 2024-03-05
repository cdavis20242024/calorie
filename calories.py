import streamlit as st
import pandas as pd
import numpy as np

st.title('Calorie Calculator')

calories = 0
col1, col2, col3 = st.columns(3)

with col1:
   st.subheader("Hamburger")
   st.subheader("Big Mac")
   st.subheader("Hot Dog")
   st.subheader("Cheese Pizza Slice")
   st.subheader("Pepperoni Slice")
   st.subheader("Ham Sandwich")
   st.subheader("PB&J Sandwich")
   st.subheader("French Fries")
   st.subheader("Can of Coke")
   st.subheader("Energy Drink")
   st.subheader("Milkshake")
   
with col2:
    st.text("")

with col3:
   calories = calories + st.number_input("burger", min_value=0, value="min", key=1, label_visibility='collapsed') * 250
   calories = calories + st.number_input("big mac", min_value=0, value="min", key=2, label_visibility='collapsed') * 563
   calories = calories + st.number_input("hot dog", min_value=0, value="min", key=3, label_visibility='collapsed') * 272
   calories = calories + st.number_input("cheese pizza", min_value=0, value="min", key=4, label_visibility='collapsed') * 277
   calories = calories + st.number_input("pepperoni pizza", min_value=0, value="min", key=5, label_visibility='collapsed') * 309
   calories = calories + st.number_input("ham sandwich", min_value=0, value="min", key=6, label_visibility='collapsed') * 447
   calories = calories + st.number_input("peanut butter", min_value=0, value="min", key=7, label_visibility='collapsed') * 376
   calories = calories + st.number_input("french fry", min_value=0, value="min", key=8, label_visibility='collapsed') * 400
   calories = calories + st.number_input("coke", min_value=0, value="min", key=9, label_visibility='collapsed') * 140
   calories = calories + st.number_input("energy drink", min_value=0, value="min", key=10, label_visibility='collapsed') * 52
   calories = calories + st.number_input("milkshake", min_value=0, value="min", key=11, label_visibility='collapsed') * 690

st.subheader("")
st.header("Calories:")
st.subheader(calories)

st.subheader("")
st.header("Time to burn calories:")
st.subheader("Walking: " + str(round(calories / 177, 2)) + " hours")
st.subheader("Running: " + str(round(calories / 596, 2)) + " hours")
st.subheader("Biking: " + str(round(calories / 650, 2)) + " hours")
st.subheader("Sitting: " + str(round(calories / 68, 2)) + " hours")
