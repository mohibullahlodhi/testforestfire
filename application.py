from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from pathlib import Path

application = Flask(__name__)
app = application

## import the models 
BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / 'models'

ridge_model = pickle.load(open(MODEL_DIR / 'ridge.pkl', 'rb'))
Standard_Scaler = pickle.load(open(MODEL_DIR / 'scaler.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/prediction', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        Tempreture = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        # Prepare input data for prediction
        input_data = np.array([[Tempreture, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        
        # Scale the input data
        scaled_input_data = Standard_Scaler.transform(input_data)
        
        # Make prediction
        prediction = ridge_model.predict(scaled_input_data)
        
        return render_template('predict.html', result=prediction[0])
    else:
        return render_template('predict.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

