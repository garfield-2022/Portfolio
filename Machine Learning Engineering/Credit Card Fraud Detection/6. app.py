#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://medium.datadriveninvestor.com/deploy-your-machine-learning-model-using-flask-made-easy-now-635d2f12c50c
"""
Created on Mon Aug  7 09:40:24 2023

@author: yingfan
"""

import numpy as np
from flask import Flask, request, render_template
import pickle

# Initialize the flask app.
app = Flask(__name__)

# Loading the saved model.
loaded_model = pickle.load(open("model.pkl", "rb"))

# Redireting the API to the home page index.html
@app.route('/')
def home():
    return render_template('index.html')

# Reading the input values and making predictions
@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        input_features = [float(x) for x in request.form.values()] 
        final_features = np.array(input_features).reshape(1, 30) 
        temp = loaded_model.predict(final_features) 
        result = temp[0]    
        
    if int(result)== 1:
        prediction ='Fraudulent'
    else:
        prediction ='Normal'            
    return render_template("result.html", prediction = prediction) 

# Run the webpage on localhost.
# Paste http://127.0.0.1:5000/ (or) http://localhost:5000 on browser and press enter.
if __name__ == "__main__":
    app.run(debug=True)