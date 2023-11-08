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

heart_disease_model = pickle.load(open('C:/Users/adnan/Downloads/Multiple Disease Prediction System-20230325T104723Z-001/Multiple Disease Prediction System/saved models/heart_disease_model.sav','rb'))

parkinson_disease_model= pickle.load(open('C:/Users/adnan/Downloads/Multiple Disease Prediction System-20230325T104723Z-001/Multiple Disease Prediction System/saved models/parkinsons_model.sav','rb'))


# sidebar for navigation
with st.sidebar:
    
   selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction','Heart Disease Prediction','Parkinson Disease Prediction' ],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')

    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    # Set normal range 
    pregnancies_normal_range=(0,17)
    glucose_normal_range = (0.000000, 199.000000)
    blood_pressure_normal_range = (0.000000, 122.000000)
    skin_thickness_normal_range=(0.000000,99.000000)
    insulin_normal_range=(0.000000,846.000000)
    bmi_normal_range=(0.000000,67.100000)
    dpf_normal_range=(0.078000,2.420000)
    age_normal_range=(21,100)

    
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


# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    #set normal range
    gender=['male','female']
    age_normal_range=(29,77)
    sex_normal_range = (0, 1)
    cp_normal_range = (0.000,3.000)
    trestbps_normal_range=(94.000,200.000)
    chol_normal_range=(126.000,564.000)
    fbs_normal_range=(0.000,1.000)
    restecg_normal_range=(0.000,2.000)
    thalach_normal_range=(71.000,202.000)
    exang_normal_range=(0.000,1.000)
    oldpeak_normal_range=(0.000,6.200)
    slope_normal_range=(0.000,2.000)
    ca_normal_range=(0.000,4.000)
    thal_normal_range=(0.000,3.000)

   
    
    with col1:
        age = st.number_input('Age', min_value=age_normal_range[0],max_value=age_normal_range[1])
        if age < age_normal_range[0] or age > age_normal_range[1]:
            st.error(f"Age should be between {age_normal_range[0]} and {age_normal_range[1]}")
            
        
    with col2:
        sex= st.number_input('Sex', min_value=sex_normal_range[0],max_value=sex_normal_range[1])
        if sex < sex_normal_range[0] or sex > sex_normal_range[1]:
             st.error(f"Gender should be either {sex_normal_range[0]} or {sex_normal_range[1]} (1=Male and 0= female)")
             
        
    with col3:
        cp = st.number_input('Chest Pain type', min_value=cp_normal_range[0],max_value=cp_normal_range[1])
        if cp < cp_normal_range[0] or cp > cp_normal_range[1]:
            st.error(f"Chest pain value should be between {cp_normal_range[0]} and {cp_normal_range[1]}")
        
    with col1:
        trestbps = st.number_input('Resting blood pressure',min_value=trestbps_normal_range[0],max_value=trestbps_normal_range[1])
        if trestbps < trestbps_normal_range[0] or trestbps > trestbps_normal_range[1]:
             st.error(f"Resting blood pressure should be between {trestbps_normal_range[0]} and {trestbps_normal_range[1]}")
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl',min_value=chol_normal_range[0], max_value=chol_normal_range[1])
        if chol < chol_normal_range[0] or chol > chol_normal_range[1]:
            st.error(f"Serum cholestoral should be between {chol_normal_range[0]} and {chol_normal_range[1]}")
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl',min_value=fbs_normal_range[0],max_value= fbs_normal_range[1] )
        if fbs < fbs_normal_range[0] or fbs > fbs_normal_range[1]:
            st.error(f"fasting blood sugar should be between {fbs_normal_range[0]} and {fbs_normal_range[1]}")
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results',min_value= restecg_normal_range[0], max_value= restecg_normal_range[1])
        if restecg < restecg_normal_range[0] or restecg > restecg_normal_range[1]:
            st.error(f"Resting cardiographic results should be between {restecg_normal_range[0]} and {restecg_normal_range[1]}")
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved',min_value= thalach_normal_range[0], max_value= thalach_normal_range[1])
        if thalach < thalach_normal_range[0] or thalach > thalach_normal_range[1]:
            st.error(f"Value should be between {thal_normal_range[0]} and  {thal_normal_range[1]}")
        
    with col3:
        exang = st.number_input('Exercise Induced Angina', min_value= exang_normal_range[0], max_value= exang_normal_range[1])
        if exang < exang_normal_range[0] or exang > exang_normal_range[1]:
            st.error(f"value should be between {exang_normal_range[0]} and {exang_normal_range[1]}")
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise',min_value=oldpeak_normal_range[0],max_value=oldpeak_normal_range[1])
        if oldpeak < oldpeak_normal_range[0] or oldpeak > oldpeak_normal_range[1]:
            st.error(f"Value should be between {oldpeak_normal_range[0]} and {oldpeak_normal_range[1]}")
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment',min_value=slope_normal_range[0],max_value=slope_normal_range[1])
        if slope < slope_normal_range[0] or slope > slope_normal_range[1]:
            st.error(f"Value should be between {slope_normal_range[0]} and {slope_normal_range[1]}")
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy',min_value=ca_normal_range[0],max_value=ca_normal_range[1])
        if ca < ca_normal_range[0] or ca > ca_normal_range[1]:
            st.error(f"Value should be between {ca_normal_range[0]} and {ca_normal_range[1]}")
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect',min_value= thal_normal_range[0], max_value= thal_normal_range[1])
        if thal < thal_normal_range[0] or thal > thal_normal_range[1]:
           st. error (f"Value should be between {thal_normal_range[0]} and {thal_normal_range[1]}")
        
        
     
     
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

 # Parkison Disease Prediction Page
if (selected == 'Parkinson Disease Prediction'):
    
    # page title
    st.title('Parkinson Disease')
    
    col1, col2, col3, col4, col5 = st.columns(5)
    #set normal range
    
    MDVPFoHz_normal_range=(88.333,260.105)
    MDVPFhiHz_normal_range = (102.145, 592.03)
    MDVPFloHz_normal_range = (65.476,239.170)

    MDVPJitter_normal_range=(0.00168,0.03316)
    MDVPJitterAbs_normal_range=(0.000007,0.00026)
    MDVPRAP_normal_range=(0.00068,0.02144)


    MDVPPQ_normal_range=(0.000920,0.01958)
    JitterDDP_normal_range=(0.00204,0.06433)
    MDVPShimmer_normal_range=(0.00954,0.11908)

    MDVPShimmerdB_normal_range=(0.085,1.302)
    ShimmerAPQ3_normal_range=(0.000,1.000)
    ShimmerAPQ5_normal_range=(0.000,1.000)

    MDVPAPQ_normal_range=(0.000,1.000)
    ShimmerDDA_normal_range=(0.01364,0.16942)
    NHR_normal_range=(0.000650,0.31482)

    HNR_normal_range=(8.441,33.047)
    RPDE_normal_range=(0.256570,0.685151)
    DFA_normal_range=(0.574282,0.825288)

    spread1_normal_range=(-7.964984,-2.434031)
    spread2_normal_range=(0.006274,0.450493)
    D2_normal_range=(1.423287,3.671155)
    PPE_normal_range=(0.044539,0.527367)

   
    
    with col1:
        MDVPFoHz = st.number_input('MDVPFo(Hz)', min_value=MDVPFoHz_normal_range[0],max_value=MDVPFoHz_normal_range[1])
        if MDVPFoHz < MDVPFoHz_normal_range[0] or MDVPFoHz > MDVPFoHz_normal_range[1]:
            st.error(f"MDVP:Fo(Hz) should be between {MDVPFoHz_normal_range[0]} and {MDVPFoHz_normal_range[1]}")
            
        
    with col2:
        MDVPFhiHz= st.number_input('MDVPFhi(Hz)', min_value=MDVPFhiHz_normal_range[0],max_value=MDVPFhiHz_normal_range[1])
        if MDVPFhiHz < MDVPFhiHz_normal_range[0] or MDVPFhiHz > MDVPFhiHz_normal_range[1]:
             st.error(f"MDVP:Fhi(Hz) should be either {MDVPFhiHz_normal_range[0]} or {MDVPFhiHz_normal_range[1]}")
             
        
    with col3:
        MDVPFloHz = st.number_input('MDVPFlo(Hz)', min_value=MDVPFloHz_normal_range[0],max_value=MDVPFloHz_normal_range[1])
        if MDVPFloHz < MDVPFloHz_normal_range[0] or MDVPFloHz > MDVPFloHz_normal_range[1]:
            st.error(f"MDVP:Flo(Hz) should be between {MDVPFloHz_normal_range[0]} and {MDVPFloHz_normal_range[1]}")
        
    with col4:
        MDVPJitter= st.number_input('MDVPJitter',min_value=MDVPJitter_normal_range[0],max_value=MDVPJitter_normal_range[1])
        if MDVPJitter< MDVPJitter_normal_range[0] or MDVPJitter > MDVPJitter_normal_range[1]:
             st.error(f"MDVP:Jitter(%) should be between {MDVPJitter_normal_range[0]} and {MDVPJitter_normal_range[1]}")
        
    with col5:
        MDVPJitterAbs = st.number_input('MDVPJitter(Abs)',min_value=MDVPJitterAbs_normal_range[0], max_value=MDVPJitterAbs_normal_range[1])
        if MDVPJitterAbs< MDVPJitterAbs_normal_range[0] or MDVPJitterAbs > MDVPJitterAbs_normal_range[1]:
            st.error(f"MDVP:Jitter(Abs) should be between {MDVPJitterAbs_normal_range[0]} and {MDVPJitterAbs_normal_range[1]}")
        
    with col1:
        MDVPRAP = st.number_input('MDVPRAP',min_value=MDVPRAP_normal_range[0],max_value= MDVPRAP_normal_range[1] )
        if MDVPRAP < MDVPRAP_normal_range[0] or MDVPRAP > MDVPRAP_normal_range[1]:
            st.error(f"MDVP:RAP should be between {MDVPRAP_normal_range[0]} and {MDVPRAP_normal_range[1]}")
        
    with col2:
        MDVPPQ = st.number_input('MDVPPPQ',min_value= MDVPPQ_normal_range[0], max_value= MDVPPQ_normal_range[1])
        if MDVPPQ < MDVPPQ_normal_range[0] or MDVPPQ > MDVPPQ_normal_range[1]:
            st.error(f"Resting NHRrdiographic results should be between {MDVPPQ_normal_range[0]} and {MDVPPQ_normal_range[1]}")
        
    with col3:
        JitterDDP = st.number_input('JitterDDP',min_value= JitterDDP_normal_range[0], max_value= JitterDDP_normal_range[1])
        if JitterDDP < JitterDDP_normal_range[0] or JitterDDP > JitterDDP_normal_range[1]:
            st.error(f"Value should be between {JitterDDP_normal_range[0]} and  {JitterDDP_normal_range[1]}")
        
    with col4:
        MDVPShimmer = st.number_input('MDVPShimmer', min_value= MDVPShimmer_normal_range[0], max_value= MDVPShimmer_normal_range[1])
        if MDVPShimmer < MDVPShimmer_normal_range[0] or MDVPShimmer > MDVPShimmer_normal_range[1]:
            st.error(f"value should be between {MDVPShimmer_normal_range[0]} and {MDVPShimmer_normal_range[1]}")
        
    with col5:
        MDVPShimmerdB = st.number_input('MDVPShimmer(dB)',min_value=MDVPShimmerdB_normal_range[0],max_value=MDVPShimmerdB_normal_range[1])
        if MDVPShimmerdB < MDVPShimmerdB_normal_range[0] or MDVPShimmerdB > MDVPShimmerdB_normal_range[1]:
            st.error(f"Value should be between {MDVPShimmerdB_normal_range[0]} and {MDVPShimmerdB_normal_range[1]}")
        
    with col1:
        ShimmerAPQ3 = st.number_input('ShimmerAPQ3',min_value=ShimmerAPQ3_normal_range[0],max_value=ShimmerAPQ3_normal_range[1])
        if ShimmerAPQ3 < ShimmerAPQ3_normal_range[0] or ShimmerAPQ3 > ShimmerAPQ3_normal_range[1]:
            st.error(f"Value should be between {ShimmerAPQ3_normal_range[0]} and {ShimmerAPQ3_normal_range[1]}")
        
    with col2:
        ShimmerAPQ5 = st.number_input('ShimmerAPQ5',min_value=ShimmerAPQ5_normal_range[0],max_value=ShimmerAPQ5_normal_range[1])
        if ShimmerAPQ5 < ShimmerAPQ5_normal_range[0] or ShimmerAPQ5 > ShimmerAPQ5_normal_range[1]:
            st.error(f"Value should be between {ShimmerAPQ5_normal_range[0]} and {ShimmerAPQ5_normal_range[1]}")

    with col3:
        MDVPAPQ=st.number_input('MDVPAPQ',min_value=MDVPAPQ_normal_range[0],max_value=MDVPAPQ_normal_range[1])
        if MDVPAPQ < MDVPAPQ_normal_range[0] or MDVPAPQ > MDVPAPQ_normal_range[1]:
            st.error(f"Value should be between {MDVPAPQ_normal_range[0]} and {MDVPAPQ_normal_range[1]}")        
        
    
    with col4:
        ShimmerDDA=st.number_input('ShimmerDDA',min_value=ShimmerDDA_normal_range[0],max_value=ShimmerDDA_normal_range[1])
        if ShimmerDDA < ShimmerDDA_normal_range[0] or ShimmerDDA > ShimmerDDA_normal_range[1]:
            st.error(f"Value should be between {ShimmerDDA_normal_range[0]} and {ShimmerDDA_normal_range[1]}")    

    
    with col5:
        NHR=st.number_input('NHR',min_value=NHR_normal_range[0],max_value=NHR_normal_range[1])
        if NHR < NHR_normal_range[0] or MDVPAPQ > NHR_normal_range[1]:
            st.error(f"Value should be between {NHR_normal_range[0]} and {NHR_normal_range[1]}")         

    with col1:
        HNR = st.number_input('HNR',min_value= HNR_normal_range[0], max_value= HNR_normal_range[1])
        if HNR < HNR_normal_range[0] or HNR > HNR_normal_range[1]:
           st. error (f"Value should be between {HNR_normal_range[0]} and {HNR_normal_range[1]}")

           
    with col2:
        RPDE = st.number_input('RPDE',min_value= RPDE_normal_range[0], max_value= RPDE_normal_range[1])
        if RPDE < RPDE_normal_range[0] or RPDE > RPDE_normal_range[1]:
           st. error (f"Value should be between {RPDE_normal_range[0]} and {RPDE_normal_range[1]}")    
        
    with col3:
        DFA = st.number_input('DFA',min_value= DFA_normal_range[0], max_value= DFA_normal_range[1])
        if DFA < DFA_normal_range[0] or DFA > DFA_normal_range[1]:
           st. error (f"Value should be between {DFA_normal_range[0]} and {DFA_normal_range[1]}")
    
    with col4:
        spread1 = st.number_input('spread1',min_value= spread1_normal_range[0], max_value= spread1_normal_range[1])
        if spread1 < spread1_normal_range[0] or spread1 > spread1_normal_range[1]:
           st. error (f"Value should be between {spread1_normal_range[0]} and {spread1_normal_range[1]}")

    with col5:
        spread2 = st.number_input('spread2',min_value= spread2_normal_range[0], max_value= spread2_normal_range[1])
        if spread2 < spread2_normal_range[0] or spread2 > spread2_normal_range[1]:
           st. error (f"Value should be between {spread2_normal_range[0]} and {spread2_normal_range[1]}")

    with col1:
        D2 = st.number_input('D2',min_value= D2_normal_range[0], max_value= D2_normal_range[1])
        if D2 < D2_normal_range[0] or D2 > D2_normal_range[1]:
           st. error (f"Value should be between {D2_normal_range[0]} and {D2_normal_range[1]}")

    with col2:
        PPE = st.number_input('PPE',min_value= PPE_normal_range[0], max_value= PPE_normal_range[1])
        if PPE < PPE_normal_range[0] or PPE > PPE_normal_range[1]:
           st. error (f"Value should be between {PPE_normal_range[0]} and {PPE_normal_range[1]}")



    # code for Prediction
    parkinson_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Parkinson Disease Test Result'):
        parkinson_prediction = parkinson_disease_model.predict([[MDVPFoHz,MDVPFhiHz,MDVPFloHz,MDVPJitter,MDVPJitterAbs,MDVPRAP,MDVPPQ,JitterDDP,MDVPShimmer,MDVPShimmerdB,ShimmerAPQ3,MDVPAPQ, ShimmerAPQ5,ShimmerDDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinson_prediction[0] == 1):
          parkinson_diagnosis = 'The person is having parkinson disease'
        else:
          parkinson_diagnosis = 'The person does not have any parkinson disease'
        
    st.success(parkinson_diagnosis)   




