# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:53:51 2022

@author: adnan
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

 diabetes_model = pickle.load(open('C:/Users/adnan/Downloads/Multiple Disease Prediction System-20230325T104723Z-001/Multiple Disease Prediction System/saved models/diabetes_model.sav', 'rb'))





# sidebar for navigation
with st.sidebar:
    
   selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction' ],
                          icons=['activity'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')

    
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    # Set normal range 
pregnancies_normal_range=(0.000000,17.000000)
glucose_normal_range = (0.000000, 199.000000)
blood_pressure_normal_range = (0.000000, 122.000000)
skin_thickness_normal_range=(0.000000,99.000000)
insulin_normal_range=(0.000000,846.000000)
bmi_normal_range=(0.000000,67.100000)
dpf_normal_range=(0.78000,2.420000)
age_normal_range=(21.000000,100.000000)

    
with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=pregnancies_normal_range[0],max_value=pregnancies_normal_range[1])
        if Pregnancies < pregnancies_normal_range[0] or Pregnancies > pregnancies_normal_range[1]:
            st.error(f"Pregnancies should be between {pregnancies_normal_range[0]} and {pregnancies_normal_range[1]}")
        

        
with col2:
        Glucose = st.number_input('Glucose Level', min_value=glucose_normal_range[0], max_value=glucose_normal_range[1])
        if Glucose < glucose_normal_range[0] or Glucose > glucose_normal_range[1]:
            st.error(f"Glucose level should be between {glucose_normal_range[0]} and {glucose_normal_range[1]}")
    
with col3:
        BloodPressure = st.number_input('Blood Pressure value', min_value=blood_pressure_normal_range[0], max_value=blood_pressure_normal_range[1])
        if BloodPressure < blood_pressure_normal_range[0] or BloodPressure > blood_pressure_normal_range[1]:
            st.error(f"Blood pressure should be between {blood_pressure_normal_range[0]} and {blood_pressure_normal_range[1]}")

    
with col1:
        SkinThickness = st.number_input('Skin Thickness value', min_value= skin_thickness_normal_range[0], max_value= skin_thickness_normal_range[1])
        if SkinThickness < skin_thickness_normal_range[0] or BloodPressure > skin_thickness_normal_range[1]:
            st.error(f"Skin Thickness should be between {skin_thickness_normal_range[0]} and {skin_thickness_normal_range[1]}")
    
with col2:
        Insulin = st.number_input('Insulin Level', min_value= insulin_normal_range[0], max_value=insulin_normal_range[1])
        if Insulin < insulin_normal_range[0] or Insulin > insulin_normal_range[1]:
              st.error(f"Insulin level should be between {insulin_normal_range[0],} and {insulin_normal_range[1]}")
    
with col3:
        BMI = st.number_input('BMI value', min_value= bmi_normal_range[0], max_value= bmi_normal_range[1])
        if BMI < bmi_normal_range[0] or BMI > bmi_normal_range[1]:
              st.error(f"BMI value should be between {bmi_normal_range[0]} and {bmi_normal_range[1]}")
    
with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value= dpf_normal_range[0],max_value=dpf_normal_range[1])
        if DiabetesPedigreeFunction< dpf_normal_range[0] or DiabetesPedigreeFunction > dpf_normal_range[1]:
              st.error(f"Diabetes Pedigree Function should be between {dpf_normal_range[0]} and {dpf_normal_range[1]}")
    
with col2:
        Age = st.number_input('Age of the Person', min_value= age_normal_range[0], max_value= age_normal_range[1])
        if Age < age_normal_range[0] or Age > age_normal_range[1]:
              st.error(f"Age should be between {age_normal_range[0]} and {age_normal_range[1]}")
    
    
    # code for Prediction
diab_diagnosis = ''
    
    # creating a button for Prediction
    
if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
st.success(diab_diagnosis)




