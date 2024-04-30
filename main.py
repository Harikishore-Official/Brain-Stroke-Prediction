import streamlit as st
from Train import load_data
from Tabs import predict


st.set_page_config(
    page_title = 'Brain Stroke Detector',
    page_icon = 'brain',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

Tabs = {
    "Prediction": predict,
}

df, X, y = load_data()

Tabs['Prediction'].app(df, X, y)
