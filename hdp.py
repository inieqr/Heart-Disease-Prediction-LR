# -*- coding: utf-8 -*-


import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved model

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Design and Implementation of an Expert System to Predict Heart Disease Using Logistic Regression',
                          
                          ['Know your heart health'],
                          icons=['heart'],
                          default_index=0)


# Heart Disease Prediction Page
if (selected == 'Know your heart health'):
    
    # page title
    st.title('Heart Disease Prediction Web App')
   
    st.write(" ")
    
    st.write("Kindly provide your information in a numerical format.")
    
    st.write(" ")
    
    st.write(" ")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input("Patient's Age in years")
        
    with col2:
        sex = st.text_input("Patient's Gender (1: Male, 0: Female)")
        
    with col3:
        cp = st.text_input("Chest Pain Type (1: Typical Angina, 2: Atypical Angina, 3: Non-Anginal Pain, 4: Asymptomatic)")
        
    with col1:
        trestbps = st.text_input("Level of blood pressure at resting mode in mm/HG")
        
    with col2:
        chol = st.text_input("Serum Cholestoral in mg/dl")
        
    with col3:
        fbs = st.text_input("Blood sugar levels on fasting (1: if FastingBS > 120 mg/dl, 0: otherwise)")
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
 
