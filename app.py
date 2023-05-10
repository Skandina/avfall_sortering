import tensorflow
import numpy as np
from tensorflow import keras
from numpy import asarray
import cv2
from PIL import Image

model_filename = "keras_model.h5"
model = tensorflow.keras.models.load_model(model_filename, compile=False)
#image = cv2.imread('13.jpeg', cv2.IMREAD_UNCHANGED)

def preprocessing(image):
    image = np.array(image)
    dim = (224,224)
    image_resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    image_normalized = (image_resized.astype(np.float32) / 127.0) - 1
    image_reshaped = image_normalized.reshape((1,224,224,3))
    return image_reshaped

def predict(image):
    prediction = model.predict(image)
    return prediction

def ai_image(image):
     
    preprocessed = preprocessing(image) 
    prediction = predict(preprocessed) 

    if cv2.waitKey(100) > 0:
        exit()

    if (prediction[0,0] >= 0.5):
        waste = "colored glass with metal cap"

    elif (prediction[0,1] >= 0.5):
        waste = "transparent glass with plastic cap"
  
    elif (prediction[0,2] >= 0.5):
        waste = "pant"

    elif (prediction[0,3] >= 0.5):
        waste = "plastic"
 
    elif (prediction[0,4] >= 0.5):
        waste = "metal can"

    elif (prediction[0,5] >= 0.5):
        waste = "metal tube with plastic cap"

    elif (prediction[0,6] >= 0.5):
        waste = "paper"

    elif (prediction[0,7] >= 0.5):
        waste = "milk package"

    elif (prediction[0,8] >= 0.5):
        waste = "transparent glass with metal cap"

    elif (prediction[0,9] >= 0.5):
        waste = "colored glass with plastic cap"

    else : 
        waste = "unknown"

    return waste

