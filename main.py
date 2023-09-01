"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st
import webbrowser

# Import necessary functions from web_functions
from web_functions import load_data

# Import pages
from Tabs import home, data, predict

# Configure the app
st.set_page_config(
    page_title = 'EEG-Eye',
    page_icon = ':wind:',
    initial_sidebar_state = 'auto'
)

# Dictionary for pages
Tabs = {
    "Home": home,
    "Data Info": data,
    "Prediction": predict
   
    
}



# Create a sidebar
# Add title to sidear
st.sidebar.title("Navigation")

# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Tabs.keys()))

st.sidebar.markdown(
    f'<a href="https://eyecare.streamlit.app/" target="_blank" style="display: inline-block; padding: 12px 20px; background-color: #4CAF50; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">Eye Care Image</a>',
    unsafe_allow_html=True
)

# Loading the dataset.
df, X, y = load_data()

# Call the app funciton of selected page to run
if page in ["Prediction"]:
    Tabs[page].app(df, X, y)
elif (page == "Data Info"):
    Tabs[page].app(df)
else:
    Tabs[page].app()
