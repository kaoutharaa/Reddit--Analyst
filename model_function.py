import re
import numpy as np
import pandas as pd
import joblib



label_map = {1: "Positive", 0: "Negative"}
loaded_model = joblib.load("C:/xampp/folder/htdocs/application_web/projet_python/model.ipynb/Logistic_Regression.pkl")
loaded_vectorizer = joblib.load("C:/xampp/folder/htdocs/application_web/projet_python/model.ipynb/vectorizer.pkl")



def resultat(text):
     
    X_new = loaded_vectorizer.transform([text])
   
  
    prediction = loaded_model.predict(X_new)
     
     
    sentiment = label_map[prediction[0]]

    return sentiment  