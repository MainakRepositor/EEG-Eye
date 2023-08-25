"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Prediction of AQI Level. However, unlike normal prediction systems, the AQI Level parameter is alone sufficient to predict the remedy. But we still suggest to work with the other parameters as well, for a better relativity.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    A = st.slider("AF3", int(df["AF3"].min()), int(df["AF3"].max()))
    B = st.slider("F7", int(df["F7"].min()), int(df["F7"].max()))
    C = st.slider("F3", int(df["F3"].min()), int(df["F3"].max()))
    D = st.slider("FC5", float(df["FC5"].min()), float(df["FC5"].max()))
    E = st.slider("T7", float(df["T7"].min()), float(df["T7"].max()))
    F = st.slider("P7", float(df["P7"].min()), float(df["P7"].max()))
    G = st.slider("O1", float(df["O1"].min()), float(df["O1"].max()))
    H = st.slider("O2", float(df["O2"].min()), float(df["O2"].max()))
    I = st.slider("P8", float(df["P8"].min()), float(df["P8"].max()))
    J = st.slider("T8", float(df["T8"].min()), float(df["T8"].max()))
    K = st.slider("FC6", float(df["FC6"].min()), float(df["FC6"].max()))
    L = st.slider("F4", float(df["F4"].min()), float(df["F4"].max()))
    M = st.slider("F8", float(df["F8"].min()), float(df["F8"].max()))
    N = st.slider("AF4", float(df["AF4"].min()), float(df["AF4"].max()))
 

    # Create a list to store all the features
    features = [A,B,C,D,E,F,G,H,I,J,K,L,M,N]

    
    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        st.info("Eye quality level detected...")

        # Print the output according to the prediction
        if (prediction == 0):
            st.success("The eye quality is good. 😎")
        elif (prediction == 1):
            st.success("The eye quality is poor. 😀")
           

        