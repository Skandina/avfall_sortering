#import tensorflow.keras
import tensorflow
import numpy as np
from tensorflow import keras
from numpy import asarray
import cv2
from PIL import Image

model_filename = "keras_model.h5"

model = tensorflow.keras.models.load_model(model_filename, compile=False)

image = cv2.imread('13.jpeg', cv2.IMREAD_UNCHANGED)

def preprocessing(image):
    dim = (224,224) 
    image_resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    image_normalized = (image_resized.astype(np.float32) / 127.0) - 1

    image_reshaped = image_normalized.reshape((1,224,224,3))

    return image_reshaped

def predict(image):
    prediction = model.predict(image)
    return prediction

while True:
    if cv2.waitKey(100) > 0:
        break

    preprocessed = preprocessing(image) 
    prediction = predict(preprocessed) 

    if (prediction[0,0] >= 0.5):
        print("this is vanillinsocker") 

    elif (prediction[0,1] >= 0.5):
        print("this is bakpulver")
  
    elif (prediction[0,2] >= 0.5):
        print("this is bikarbonat") 
    
    else : 
        print("can't recognize what it is")

    print(prediction)
    break
