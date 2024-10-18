import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

Typhoid_project = pickle.load(open('Typhoid_model.sav', 'rb'))
# page title
st.title('Typhoid Disease Prediction using ML')


# getting the input data from the user
col1, col2, col3,col4, col5 = st.columns(5)

with col1:
    Fever = st.text_input('Fever')
    
with col2:
    Cough = st.text_input('Cough')

with col3:
    Abdominal_Pain = st.text_input('Abdominal_Pain')
    
with col4:
    Nausea = st.text_input('Nausea')
    
with col5:
    Vomiting = st.text_input('Vomiting')

with col1:
    Body_Temperature_High = st.text_input('Body_Temperature_High')
    
with col2:
    Diarrhea = st.text_input('Diarrhea')

with col3:
    Loss_of_Appetite = st.text_input('Loss_of_Appetite')

with col4:
    Weakness = st.text_input('Weakness')

# code for Prediction
Typhoid_diagnosis = ''

# creating a button for Prediction

if st.button('Typhoid Disease Test Button'):
    try:
        Typhoid_disease_prediction = Typhoid_project.predict([[Fever,Cough,Abdominal_Pain,Nausea,Vomiting,Body_Temperature_High,Diarrhea,Loss_of_Appetite,Weakness]])
    except ValueError as e:
        st.error(f"Prediction error: {str(e)}")
    
    if (Typhoid_disease_prediction[0] == 1):
      Typhoid_diagnosis = 'The person is effected with Typhoid'
    else:
      Typhoid_diagnosis = 'The person is not effected with Typhoid'
    
st.success(Typhoid_diagnosis)
