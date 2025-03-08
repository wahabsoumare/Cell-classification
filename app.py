import numpy as np
from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array

import os
import shutil

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'

def clean_upload_folder():
    if os.path.exists(UPLOAD_FOLDER) :
        shutil.rmtree(UPLOAD_FOLDER)
    os.makedirs(UPLOAD_FOLDER)

model = load_model('models/best_prediction_model_for_paludisme.keras')

def predict_class(path):
    image = load_img(path, target_size = (180, 180))
    image_array = img_to_array(image)
    image_array = np.expand_dims(image_array, axis = 0)
    # image_array /= 255.0

    class_names = ['Parasitized', 'Uninfected']
    prediction = model.predict(image_array, verbose = 0)[0][0]
    predicted_class = class_names[int(prediction > 0.5)]

    return round(prediction, 2), predicted_class

@app.route('/', methods = ['GET', 'POST'])
def predict():
    clean_upload_folder()
    predictions = []

    if request.method == 'POST' :
        if 'file' not in request.files :
            return "No file has been sent."
        
        files = request.files.getlist('file')
        if not files or files[0].filename == '' :
            return "No files selected."

        for file in files : 
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            probability, class_predict = predict_class(filepath)
            predictions.append((f"uploads/{file.filename}", class_predict, probability))
        return render_template('index.html', predictions = predictions)
    
    return render_template('index.html')

if __name__ == '__main__' :
    app.run(debug = True)