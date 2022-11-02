import pickle
import numpy as np
import streamlit as st
from enum import Enum

# loading the model
model_path = "saved_model/heart_disease_model.sav"
model = pickle.load(open(model_path, "rb"))

# options
Gender = {0: "Female", 1: "Male"}
ChestPain = {0: "Typical Angina", 1: "Atypical Angina", 2: "Non Anginal Pain", 3: "Asymptomatic"}
FastingBloodSugar = {0: "Less than 120 mg/dl", 1: "Greater than 120 mg/dl"}
ElectrocardiographicResult = {0: "Normal", 1: "ST-T Wave Abnormality", 2: "Left Ventricular Hypertrophy"}
ExerciseInducedAngina = {0: "No", 1: "Yes"}
Slope = {0: "Upsloping", 1: "Flat", 2:"Downsloping"}
Thal = {0: "Normal", 1: "Fixed Defect", 2:"Reversable Defect"}

def format_func(dct_name,option):
    return dct_name[option]

def get_heart_disease_status(input_data):

    input_data_arr= np.asarray(input_data)
    
    input_data_reshaped = input_data_arr.reshape(1, -1)
    
    status = model.predict(input_data_reshaped)

    if status[0] == 1:
        return 'High Risk of heart disease'
    else:
        return 'Low Risk of heart disease'
    

def main():
    # tite for the app
    st.set_page_config(page_title="Heart Disease Prediction", page_icon="🫀", layout="centered")
    st.title("🫀 Heart Disease Prediction")
    
    # getting input data from user
    form = st.form(key="annotation")

    with form:
        cols = st.columns((1, 1))
        age = cols[0].number_input("Age:", min_value=0,  value=0, step=1)
        sex = cols[1].selectbox("Gender:", Gender.keys(), format_func=lambda x:Gender[ x ])
        cp = cols[0].selectbox("Chest Pain:", ChestPain.keys(), format_func=lambda x:ChestPain[ x ])
        trestbps = cols[1].number_input("Resting Blood Pressure:", min_value=0,  value=0, step=1)
        chol = cols[0].number_input("Serum Cholestrol:", min_value=0,  value=0, step=1)
        fbs = cols[1].selectbox("Fasting Blood Sugar:", FastingBloodSugar.keys(), format_func=lambda x:FastingBloodSugar[ x ])
        restecg = cols[0].selectbox("Electrocardiographic Result:", ElectrocardiographicResult.keys(), format_func=lambda x:ElectrocardiographicResult[ x ])
        thalach = cols[1].number_input("Maximum Heart Rate Achieved:", min_value=0,  value=0, step=1)
        exang = cols[0].selectbox("Exercise Induced Angina:", ExerciseInducedAngina.keys(), format_func=lambda x:ExerciseInducedAngina[ x ])
        oldpeak = cols[1].number_input("ST depression induced by exercise relative to rest:", min_value=0.0,  value=0.0)
        slope = cols[0].selectbox("Slope:", Slope.keys(), format_func=lambda x:Slope[ x ])
        ca = cols[1].slider('Vessels colored by flourosopy', 0, 3, 1)
        thal = cols[0].selectbox("Thal:", Thal.keys(), format_func=lambda x:Thal[ x ])
        submitted = st.form_submit_button(label="Analyze")

    # code for prediction
    status = ""
    
    # create a button
    if submitted:

        status = get_heart_disease_status([age, sex, cp, trestbps, chol, fbs, 
                                           restecg, thalach, exang, oldpeak, 
                                           slope, ca, thal])
        st.success(status)

if __name__ == "__main__":
    main()
