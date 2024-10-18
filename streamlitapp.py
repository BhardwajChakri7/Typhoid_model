import pickle
import streamlit as st

# loading the saved models
Typhoid_project = pickle.load(open('Typhoid_model.sav', 'rb'))

# page title
st.title('Typhoid Disease Prediction using ML')

# Adding custom styles
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://raw.githubusercontent.com/SHAIK-RAIYAN-2022-CSE/malaria/main/Images-free-abstract-minimalist-wallpaper-HD.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    [data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0);
    }
    .block-container {
        background: rgba(0, 0, 0, 0.6);
        padding: 30px;
        border-radius: 15px;
        max-width: 800px;
        margin: auto;
        backdrop-filter: blur(10px);
        box-shadow: 0px 8px 30px rgba(0, 0, 0, 0.7);
    }
    .stButton>button {
        background-color: #FF6347;
        color: white;
        font-size: 18px;
        padding: 12px 30px;
        border-radius: 10px;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: white;
        color: #FF6347;
        border: 2px solid #FF6347;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    input[type="text"], input[type="number"], select {
        background-color: white !important;
        color: black !important;
        border: 1px solid #FF6347;
        border-radius: 5px;
        padding: 12px;
        width: 100%;  /* Make the input box full width */
        box-sizing: border-box;  /* Include padding in width */
    }
    select {
        height: 45px; /* Adjust height for consistency */
        -webkit-appearance: none; /* Remove default styling */
        -moz-appearance: none; /* Remove default styling */
        appearance: none; /* Remove default styling */
    }
    </style>
    """, unsafe_allow_html=True
)

# getting the input data from the user
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    Fever = st.number_input('Fever (°F)', min_value=95, max_value=105, value=101, step=1)
    
with col2:
    Cough = st.selectbox('Cough', options=['No', 'Mild', 'Severe'], index=0)

with col3:
    Abdominal_Pain = st.selectbox('Abdominal Pain', options=['No', 'Yes'], index=0)
    
with col4:
    Nausea = st.selectbox('Nausea', options=['No', 'Yes'], index=0)
    
with col5:
    Vomiting = st.selectbox('Vomiting', options=['No', 'Yes'], index=0)

with col1:
    Body_Temperature_High = st.number_input('Body Temperature High (°F)', min_value=95, max_value=105, value=102, step=1)
    
with col2:
    Diarrhea = st.selectbox('Diarrhea', options=['No', 'Yes'], index=0)

with col3:
    Loss_of_Appetite = st.selectbox('Loss of Appetite', options=['No', 'Yes'], index=0)

with col4:
    Weakness = st.selectbox('Weakness', options=['No', 'Yes'], index=0)

# code for Prediction
Typhoid_diagnosis = ''

# creating a button for Prediction
if st.button('Typhoid Disease Test Button'):
    try:
        Typhoid_disease_prediction = Typhoid_project.predict([[Fever, Cough, Abdominal_Pain, Nausea, Vomiting, Body_Temperature_High, Diarrhea, Loss_of_Appetite, Weakness]])
    except ValueError as e:
        st.error(f"Prediction error: {str(e)}")
    
    if (Typhoid_disease_prediction[0] == 1):
        Typhoid_diagnosis = 'The person is affected with Typhoid'
    else:
        Typhoid_diagnosis = 'The person is not affected with Typhoid'
    
st.success(Typhoid_diagnosis)
