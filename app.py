from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Model load karna
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    print("Error: Pehle train_model.py run karke model generate karo!")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # User se data lena
            temp = float(request.form['temperature'])
            time = float(request.form['time'])
            
            # Prediction karna
            features = np.array([[temp, time]])
            prediction = model.predict(features)
            predicted_usage = round(prediction[0], 2)
            
            # SMART CONTROLLER LOGIC
            # Agar usage 3.5 KwH se zyada hai toh Grid use karo, warna Solar
            source = "Main Grid (Heavy Load)" if predicted_usage > 3.5 else "Solar/Battery (Eco Mode)"
            color = "red" if predicted_usage > 3.5 else "green"

            return render_template('index.html', 
                                   prediction_text=f'Expected Load: {predicted_usage} kW/h',
                                   controller_status=f'Recommended Source: {source}',
                                   status_color=color)
        except Exception as e:
            return render_template('index.html', prediction_text="Error in input.")

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)