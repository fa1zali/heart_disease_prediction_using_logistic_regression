### Date created
31st Oct 2022

### Project Title
**Heart Disease Prediction using Logistic Regression**

### Description
Logistic Regression is a regression approach used for predicting only two possible values.

For this project, we will be building a machine learning model to classify whether the person is at *HIGH* or *LOW* risk of a heart disease based on certain medical diagnostic records included in the dataset. Our goal is to work through this notebook by collecting data, preprocessing it, splitting it into testing and training datasets, train the model and evaluate the accuracy of our model.

**API**

We have created an API using FastAPI for users to interact with.
You can run the model using uvicorn on your local machine and test the API, refer to heart_disease_api.py.

```
uvicorn heart_disease_api:app --reload
```

**StreamLit Web App**

We also created a simple web app using Streamlit.
You can run the app on your local machine using StreamLit and test the web app, refer to heart_disease_streamlit.py.

```
streamlit run heart_disease_streamlit.py
```

The app is deployed on Strealit.io. Use following link to explore: [Heart Disease Prediction WebApp](https://fa1zali-heart-disease-webapp-heart-disease-streamlit-g4hz6s.streamlitapp.com/)

### Files used
We used the following dataset available on Kaggle to work on this project:

* [Heart Disease Cleveland UCI](https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci)

The datasets consists of several medical records as predictor variables and one target variable. Predictor variables includes the age, gender, chest pain, resting blood pressure, serum cholestoral, fasting blood sugar, resting electrocardiographic results and so on.

### Credits
Thanks to Kaggle for teaching me ML :sparkles: :heart: :sparkles:
