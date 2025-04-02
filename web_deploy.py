# -*- coding: utf-8 -*-
 """Web_Deploy.ipynb
 
 Automatically generated by Colab.
 
 Original file is located at
     https://colab.research.google.com/drive/1xBPp2ermh0xM72pDyff0ACgmElQiwtdl
 """
 
 import streamlit as st
 import pickle
 import pandas as pd
 import numpy as np
 from sklearn.preprocessing import StandardScaler
 
 # Load model
 model = pickle.load(open("QualCheck.pkl", "rb"))
 scaler = StandardScaler()
 
 # Streamlit UI
 st.title("Wine Quality Prediction")
 st.write("Geser slider untuk mengatur nilai fitur dan prediksi kualitas wine:")
 
 # Input fields using sliders
 fixed_acidity = st.slider("Fixed Acidity", 0.0, 15.0, 7.0)
 volatile_acidity = st.slider("Volatile Acidity", 0.0, 2.0, 0.5)
 citric_acid = st.slider("Citric Acid", 0.0, 1.5, 0.3)
 residual_sugar = st.slider("Residual Sugar", 0.0, 15.0, 2.0)
 chlorides = st.slider("Chlorides", 0.0, 0.2, 0.08)
 free_sulfur_dioxide = st.slider("Free Sulfur Dioxide", 0.0, 80.0, 30.0)
 total_sulfur_dioxide = st.slider("Total Sulfur Dioxide", 0.0, 300.0, 100.0)
 density = st.slider("Density", 0.98, 1.005, 0.995)
 pH = st.slider("pH", 2.5, 4.0, 3.2)
 sulphates = st.slider("Sulphates", 0.3, 2.0, 0.9)
 alcohol = st.slider("Alcohol", 8.0, 15.0, 10.0)
 
 # Predict button
 if st.button("Predict Quality"):
     try:
         # Prepare input data
         features = np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                               chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,
                               pH, sulphates, alcohol]])
         df = pd.DataFrame(features, columns=['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
                                              'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
                                              'pH', 'sulphates', 'alcohol'])
 
         # Scale input data
         df[df.columns] = scaler.fit_transform(df[df.columns])
 
         # Make prediction
         prediction = model.predict(df)
 
         # Display result
         st.success(f"Predicted Wine Quality: {int(prediction[0])}")
     except Exception as e:
         st.error(f"Error: {str(e)}")
