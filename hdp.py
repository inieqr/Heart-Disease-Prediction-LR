# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved model

loaded_model = pickle.load(open('trained_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Design and Implementation of an Expert System to Predict Heart Disease Using Logistic Regression',
                          
                          ['Know your heart health'],
                          icons=['heart'],
                          default_index=0)


# Heart Disease Prediction Page

def main():
    
    # page title
    st.title('Heart Disease Prediction Web App')
   
    st.write(" ")
    
    st.write("Kindly provide your information in a numerical format.")
    
    st.write(" ")
    
    st.write(" ")

    col1, col2, col3, = st.columns(3)
    
    with col1:
        age = st.text_input("Age (in years)")
        
    with col2:
        sex = st.text_input("Sex (1: Male, 0: Female)")
        
    with col3:
        chest_pain_type = st.text_input("Chest Pain Type (1: Typical Angina, 2: Atypical Angina, 3: Non-Anginal Pain, 4: Asymptomatic)")
        
    with col1:
        resting_blood_pressure = st.text_input("Level of blood pressure at resting mode in mm/HG")
        
    with col2:
        cholesterol = st.text_input("Serum Cholestoral in mg/dl")
        
    with col3:
        fasting_blood_sugar = st.text_input("Blood sugar levels on fasting > 120 mg/dl (1: True, 0: False)")
        
    with col1:
        rest_ecg = st.text_input("Resting electrocardiographic results (0 : Normal, 1: Abnormality in ST-T wave, 2: Left ventricular hypertrophy)")
        
    with col2:
        max_heart_rate_achieved = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exercise_induced_angina = st.text_input("Angina induced by exercise (1: Yes, 0: No)")
        
    with col1:
        st_depression = st.text_input("ST depression induced by exercise relative to rest")
        
    with col2:
        st_slope = st.text_input("Slope of the peak exercise ST segment (1: upsloping, 2: flat, 3: downsloping)")
        
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = loaded_model.predict([[age,sex,chest_pain_type,resting_blood_pressure,cholesterol,fasting_blood_sugar,rest_ecg,max_heart_rate_achieved,exercise_induced_angina,st_depression,st_slope]])
        
        
        if (heart_prediction[0] == 0):
          heart_diagnosis = 'This patient does not have any heart disease'
        else:
          heart_diagnosis = 'This patient has heart disease'
        
    st.success(heart_diagnosis)
    
    # Add "Restart" button to sidebar
if st.sidebar.button('Restart'):
    st.experimental_rerun()
        
if __name__ == '__main__':
    main()
    
