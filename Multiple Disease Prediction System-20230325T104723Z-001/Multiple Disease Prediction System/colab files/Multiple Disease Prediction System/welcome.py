import streamlit as st

def show_welcome():
    st.title("Welcome to the Diabetes Prediction App!")
    st.write("This app uses machine learning to predict whether a person has diabetes or not.")
    st.write("To get started, click the button below.")

    if st.button("Get started"):
        # Redirect the user to the diabetes prediction page
        st.experimental_set_query_params(page="diabetes_prediction")

