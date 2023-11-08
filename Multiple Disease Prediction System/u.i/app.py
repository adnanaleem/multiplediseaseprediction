import streamlit as st
import welcome
import multiple_disease_pred

def main():
    st.set_page_config(page_title="Diabetes Prediction App", page_icon=":bar_chart:")
    page = st.experimental_get_query_params().get("page")

    if page != "welcome":
        # Show the welcome page by default
        welcome.show_welcome()
    else:
        # Show the diabetes prediction page
        welcome.show_welcome()




