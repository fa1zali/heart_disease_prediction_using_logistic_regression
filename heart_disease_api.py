# import modules
import pickle
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
import json
import numpy as np

# loading the model
model_path = "saved_model/heart_disease_model.sav"
model = pickle.load(open(model_path, "rb"))

# Initializing FastAPI
app = FastAPI()

class Gender(int,Enum):
    female = 0
    male = 1

class ChestPain(int,Enum):
    typical_angina = 0 
    atypical_angina = 1
    non_anginal_pain = 2
    asymptomatic = 3

class FastingBloodSugar(int, Enum):
    negative = 0
    positive = 1


class ElectrocardiographicResult(int,Enum):
    normal = 0
    st_t_wave_abnormality = 1
    left_ventricular_hypertrophy = 2

class ExerciseInducedAngina(int, Enum):
    negative = 0
    positive = 1

class Slope(int, Enum):
    upsloping = 0 
    flat = 1
    downsloping = 2

class ColoredVessels(int, Enum):
    zero = 0 
    one = 1
    two = 2
    three = 3

class Thal(int, Enum):
    normal = 0
    fixed_defect = 1
    reversable_defect = 2

class MedicalParameters(BaseModel):
    age : int
    sex : Gender
    cp : ChestPain
    trestbps : int
    chol : int
    fbs : FastingBloodSugar
    restecg : ElectrocardiographicResult
    thalach : int
    exang : ExerciseInducedAngina
    oldpeak : float
    slope : Slope
    ca : ColoredVessels
    thal : Thal

@app.post("/get_heart_disease_status")
def get_heart_disease_status(input_parameters:MedicalParameters):
    input_data = input_parameters.json()
    input_dct = json.loads(input_data)

    a = input_dct["age"]
    b = input_dct["sex"]
    c = input_dct["cp"]
    d = input_dct["trestbps"]
    e = input_dct["chol"]
    f = input_dct["fbs"]
    g = input_dct["restecg"]
    h = input_dct["thalach"]
    i = input_dct["exang"]
    j = input_dct["oldpeak"]
    k = input_dct["slope"]
    l = input_dct["ca"]
    m = input_dct["thal"]

    input_list = [a,b,c,d,e,f,g,h,i,j,k,l,m]
    input_data_arr = np.asarray(input_list)
    input_data_reshaped = input_data_arr.reshape(1, -1)

    status = model.predict(input_data_reshaped)

    if status[0] == 1:
        return {'status': f'High Risk of heart disease'}
    else:
        return {'status': f'Low Risk of heart disease'}