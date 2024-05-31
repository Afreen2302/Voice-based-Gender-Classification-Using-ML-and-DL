from flask import Flask, jsonify, request 
from flask_cors import CORS
import joblib
import pandas as pd
import os
from audiodataextraction import extract_audio_features

loaded_model = joblib.load('model.pkl')
app = Flask(__name__) 
CORS(app)
path=['',]

@app.route('/', methods = ['GET', 'POST']) 
def home(): 
	if(request.method == 'GET'): 
		data = "hello world"
		return jsonify({'data': data}) 
     
@app.route("/upload", methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename != '':
            upload_folder = 'path'
            os.makedirs(upload_folder, exist_ok=True)
            file_path = os.path.join(upload_folder, file.filename)
            file.save(file_path)
            path[0]=file_path
            return "File uploaded successfully"
        else:
            return "No file uploaded"
        
@app.route('/prediction', methods=['POST'])
def predict():
    try:
        input_data = extract_audio_features(path[0])
        input_df = pd.DataFrame(input_data)
        predictions = loaded_model.predict(input_df)
        if predictions==[1]:
            response = {'prediction':'male'}
        elif predictions==[0]:
            response = {'prediction':'female'}
        else:
            response = {'predictions':"Can't Predict"}
        return jsonify(response)
        
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__': 
	app.run(debug = True) 
