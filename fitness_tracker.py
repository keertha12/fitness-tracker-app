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
st.markdown("### **Inputs**")

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

def calculate_fitness(steps, sun, water):
    issues = []
    
    # Check each metric and add specific feedback
    if not (12000 <= steps <= 15000):
        if steps < 2000:
            issues.append("Daily Steps: Need to walk much more")
        elif steps < 5000:
            issues.append("Daily Steps: Need to walk more")
        elif steps < 7000:
            issues.append("Daily Steps: Below average")
        elif steps < 12000:
            issues.append("Daily Steps: Good, but aim for higher")

    if not (25 <= sun <= 30):
        if sun < 5:
            issues.append("Sun Exposure : Too low")
        elif sun < 15:
            issues.append("Sun Exposure : Average, aim for more")
        elif sun < 25:
            issues.append("Sun Exposure : Good, but aim for higher")
    
    if water < 5:
        if water < 2:
            issues.append("Water Intake: Critically low")
        elif water < 3:
            issues.append("Water Intake: Below average")
        elif water < 4:
            issues.append("Water Intake: Average, aim for higher")
        elif water < 5:
            issues.append("Water Intake: Good, but aim for higher")
    
    # If no issues, assign Excellent, Good, Average, or Needs Improvement
    if not issues:
        if 12000 <= steps <= 15000 and 25 <= sun <= 30 and water >= 5:
            return "Excellent"
        elif 7000 <= steps <= 11999 and 15 <= sun <= 24 and water >= 4:
            return "Good"
        elif 5000 <= steps <= 6999 and 5 <= sun <= 14 and water >= 3:
            return "Average"
        elif 2000 <= steps <= 4999 and sun < 5 and water >= 2:
            return "Need to Improve"
    
    # Combine all issues and return feedback
    return "Need to Improve\n" + "\n".join(issues)



# Calculate Result
fitness_result = calculate_fitness(daily_steps, sun_exposure, water_intake)

# Display Result
st.markdown(f"## Fitness Level: **{fitness_result}**")


