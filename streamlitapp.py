import pickle
import streamlit as st

# loading the saved models
Typhoid_project = pickle.load(open('Typhoid_model.sav', 'rb'))

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
        border: 2px solid #ccc;
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
        width: 100%;
        box-sizing: border-box;
    }
    select {
        height: 45px;
        appearance: none;
    }
    </style>
    """, unsafe_allow_html=True
)

# Page title
st.title('Typhoid Disease Prediction using ML')

# Location input
state = st.selectbox(
    'Select your location (Indian State)', 
    ['', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
     'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka',
     'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
     'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
     'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
)

# Input data collection
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

# Encode categorical inputs
def encode_input(value):
    if value == 'Yes':
        return 1
    elif value == 'No':
        return 0
    elif value == 'Mild':
        return 0.5
    elif value == 'Severe':
        return 2
    return value

# Prediction logic
Typhoid_diagnosis = ''

# Prediction button
if st.button('Typhoid Disease Test Button'):
    if state == '':
        st.error("Please select your location.")
    else:
        try:
            prediction = Typhoid_project.predict([[
                Fever, encode_input(Cough), encode_input(Abdominal_Pain),
                encode_input(Nausea), encode_input(Vomiting), Body_Temperature_High,
                encode_input(Diarrhea), encode_input(Loss_of_Appetite), encode_input(Weakness)
            ]])
            Typhoid_diagnosis = 'The person is affected with Typhoid' if prediction[0] == 1 else 'The person is not affected with Typhoid'
        except ValueError as e:
            st.error(f"Prediction error: {str(e)}")

# Display diagnosis result
st.success(Typhoid_diagnosis)
