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

    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        age = st.text_input("Age (in years)")
        
    with col2:
        sex = st.text_input("Sex (1: Male, 0: Female)")
        
    with col3:
        cp = st.text_input("Chest Pain Type (0: Typical Angina, 1: Atypical Angina, 2: Non-Anginal Pain, 3: Asymptomatic)")
        
    with col4:
        trestbps = st.text_input("Level of blood pressure at resting mode in mm/HG")
        
    with col1:
        chol = st.text_input("Serum Cholestoral in mg/dl")
        
    with col2:
        fbs = st.text_input("Blood sugar levels on fasting > 120 mg/dl (1: True, 0: False)")
        
    with col3:
        restecg = st.text_input("Resting electrocardiographic results (0 : Normal, 1: Abnormality in ST-T wave, 2: Left ventricular hypertrophy)")
        
    with col4:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col1:
        exang = st.text_input("Angina induced by exercise (1: Yes, 0: No)")
        
    with col2:
        oldpeak = st.text_input("ST depression induced by exercise relative to rest")
        
    with col3:
        slope = st.text_input("Slope of the peak exercise ST segment (1: upsloping, 2: flat, 3: downsloping)")
        
    with col4:
        ca = st.text_input("Major vessels colored by flourosopy (0-3)")
        
    with col1:
        thal = st.text_input("Thalassemia (0: normal, 1: fixed defect, 2: reversable defect)")
        
     
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
        
 
