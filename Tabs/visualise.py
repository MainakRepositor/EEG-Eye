"""This modules contains data about visualisation page"""

# Import necessary modules
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# Import necessary functions from web_functions
from web_functions import train_model

def app(df, X, y):
    """This function create the visualisation page"""
    
    # Remove the warnings
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Set the page title
    st.title("Visualise the AQI Level")

    # Create a checkbox to show correlation heatmap
    if st.checkbox("Show the correlation heatmap"):
        st.subheader("Correlation Heatmap : How each parameter affects the others")

        fig = plt.figure(figsize = (10, 6))
        ax = sns.heatmap(df.iloc[:, 1:].corr(), annot = True)   # Creating an object of seaborn axis and storing it in 'ax' variable
        bottom, top = ax.get_ylim()                             # Getting the top and bottom margin limits.
        ax.set_ylim(bottom + 0.5, top - 0.5)                    # Increasing the bottom and decreasing the top margins respectively.
        st.pyplot(fig)

    if st.checkbox("Show Scatter Plot"):
        st.subheader("How concentrations affect AQI")
        figure, axis = plt.subplots(2, 2,figsize=(15,10))

        sns.scatterplot(ax=axis[0,0],data=df,x='no2',y='aqi')
        axis[0, 0].set_title("Nitrogen Dioxide vs AQI")
  
        sns.scatterplot(ax=axis[0,1],data=df,x='so2',y='aqi')
        axis[0, 1].set_title("Sulphur Dioxide vs AQI")
  
        sns.scatterplot(ax=axis[1, 0],data=df,x='co',y='aqi')
        axis[1, 0].set_title("Carbon Monoxide vs AQI")
  
        sns.scatterplot(ax=axis[1,1],data=df,x='pm2_5',y='aqi')
        axis[1, 1].set_title("Particulate Matter vs AQI")
        st.pyplot()

    if st.checkbox("Display Boxplot"):
        st.subheader("Distribution of AQI determiners in air sample")
        fig, ax = plt.subplots(figsize=(15,5))
        df.boxplot(['so2', 'no2', 'o3','nh3','co','pm2_5'],ax=ax)
        st.pyplot()

    if st.checkbox("Show Sample Results"):
        st.subheader("General AQI trend around the world")
        safe = (df['AQI_Range'] == 1).sum()
        low = (df['AQI_Range'] == 2).sum()
        med = (df['AQI_Range'] == 3).sum()
        high = (df['AQI_Range'] == 4).sum()
        vhigh = (df['AQI_Range'] == 5).sum()
        data = [safe,low,med,high,vhigh]
        labels = ['Good', 'Moderate','Unhealthy','Poor','Hazardous']
        colors = sns.color_palette('pastel')[0:5]
        plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
        st.pyplot()

    
   