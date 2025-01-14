# app.py
import pandas as pd
import os
import pickle
from flask import Flask, request, render_template, jsonify

# Update the dataset path to the 'dataset' folder
data_path = 'C:/Users/Karti/Documents/Projects/Fake Job Recuirment Prediction/fake_job_postings.csv'
data = pd.read_csv(data_path)


model_path1 = r'C:\Users\Karti\Documents\Projects\Fake Job Recuirment Prediction\model\job_post_detector.pkl'

model_path2 = r'C:\Users\Karti\Documents\Projects\Fake Job Recuirment Prediction\model\vectorizer.pkl'
# Load model and vectorizer
with open(model_path1, 'rb') as f: 
    model = pickle.load(f)

with open(model_path2, 'rb') as f:  
    vectorizer = pickle.load(f)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    job_description = request.form['job_description']
    print(f"Job Description: {job_description}")  # Debugging line
    
    if not job_description:
        return jsonify({'error': 'No job description provided'}), 400

    vectorized_input = vectorizer.transform([job_description])
    prediction = model.predict(vectorized_input)
    result = 'Genuine' if prediction[0] == 0 else 'Fake'
    
    print(f"Prediction: {result}")  # Debugging line

    if request.is_json:
        return jsonify({'result': result})
    return render_template('result.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
