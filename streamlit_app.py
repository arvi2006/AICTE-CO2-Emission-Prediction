
import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('/content/drive/MyDrive/final_forecasting_co2_emmision.pkl')  # Ensure this file exists in the same directory

# Define input features used in the model
selected_features = ['gdp', 'population', 'energy_use']  # Replace with actual feature names

# Streamlit app UI
st.title("Carbon Emissions Prediction App")
st.write("Enter values for each feature to predict CO₂ emissions per capita.")

# Collect input for each feature
input_data = {}
for feature in selected_features:
    input_data[feature] = st.number_input(f"Enter {feature}", value=0.0)

# Convert inputs to DataFrame
input_df = pd.DataFrame([input_data])

# Make prediction
if st.button("Predict"):
    prediction = model.predict(input_df)
    st.success(f"Predicted CO₂ emissions per capita: {prediction[0]:.2f}")
