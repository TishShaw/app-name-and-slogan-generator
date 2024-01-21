import streamlit as st
import LangChainHelper

st.title("App Name and Slogan Generator")

app_type = st.sidebar.selectbox("Choose app type: ", ("E-commerce", "Social Networking", "Travel", "Fitness", "Productivity", "Food Delivery"))


if app_type:
    response = LangChainHelper.generate_app_name_and_slogan(app_type)
    st.header(response['app_name'].strip())
    st.write(response['slogan'].strip())

