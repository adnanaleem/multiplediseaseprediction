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