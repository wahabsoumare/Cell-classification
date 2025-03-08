import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array

model = load_model('models/prediction-model-for-malaria-infected-cells.h5')

def predict(path):
    image = load_img(path, target_size = (180, 180))
    image_array = img_to_array(image)
    image_array = np.expand_dims(image_array, axis = 0)
    # image_array /= 255.0

    class_names = ['Parasitized', 'Uninfected']
    prediction = model.predict(image_array, verbose = 0)[0][0]
    predicted_class = class_names[int(prediction > 0.5)]

    return prediction, predicted_class
    
if __name__ == '__main__' :
    image = 'data/Parasitized/test1.jpg'
    probability, class_predict = predict(image)
    print(f'Class predict : {class_predict} with probability to be Uninfected {probability:.2f}')
