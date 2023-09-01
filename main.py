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

url = "https://eyecare.streamlit.app/"
st.sidebar.button('Eyecare Image'):
    webbrowser.open_new_tab(url)    

# Create a sidebar
# Add title to sidear
st.sidebar.title("Navigation")

# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Tabs.keys()))


# Loading the dataset.
df, X, y = load_data()

# Call the app funciton of selected page to run
if page in ["Prediction"]:
    Tabs[page].app(df, X, y)
elif (page == "Data Info"):
    Tabs[page].app(df)
else:
    Tabs[page].app()
