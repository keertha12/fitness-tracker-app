# -*- coding: utf-8 -*-
"""fitness_tracker.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ltRJl1D0SWn50tVXgQvbkEM0SGhuaN_A
"""


import streamlit as st
import matplotlib.pyplot as plt

# Application Title
st.title("Fitness Tracker")

# Input Section Heading
st.markdown("### **Inputs (in Metric Form)**")

# Input Data Columns
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    age = st.number_input("Age (years)", min_value=10, max_value=60, step=1)

with col2:
    daily_steps = st.number_input("Daily Steps", min_value=2500, max_value=15000, step=100)

with col3:
    sun_exposure = st.number_input("Sun Exposure (mins)", min_value=0, max_value=30, step=1)

with col4:
    water_intake = st.number_input("Water Intake (Liters)", min_value=0.5, max_value=7.0, step=0.1)

# Fitness Calculator
def calculate_fitness(steps, sun, water):
    if 12000 <= steps <= 15000 and 25 <= sun <= 30 and water >= 5:
        return "Excellent"
    elif 7000 <= steps <= 11999 and 15 <= sun <= 24 and water >= 4:
        return "Good"
    elif 5000 <= steps <= 6999 and 5 <= sun <= 14 and water >= 3:
        return "Average"
    elif 2000 <= steps <= 4999 and sun < 5 and water >= 2:
        return "Need to Improve"
    else:
        if steps >= 12000:
            return "Excellent"
        elif 7000 <= steps <= 11999:
            return "Good"
        elif 5000 <= steps <= 6999:
            return "Average"
        elif 2000 <= steps <= 4999:
            return "Need to Improve"
        else:
            return "Poor"

# Calculate Result
fitness_result = calculate_fitness(daily_steps, sun_exposure, water_intake)

# Display Result
st.markdown(f"## Fitness Level: **{fitness_result}**")

# Data Visualization
st.markdown("### **Fitness Level Visualization**")
data = {
    "Metric": ["Daily Steps", "Sun Exposure", "Water Intake"],
    "Input Value": [daily_steps, sun_exposure, water_intake],
    "Ideal Range": [
        "12,000-15,000",
        "25-30 mins",
        ">= 5 Liters"
    ]
}


