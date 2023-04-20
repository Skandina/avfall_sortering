import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import mysql.connector
from mysql.connector import Error
import secret 
from app import ai_image
from data_connect import how_to_sort
import cv2


app = Flask(__name__)

UPLOAD_FOLDER = '/home/separk/sortering/img_data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

HEX_SEC_KEY = secret.secret_key()
app.config['SECRET_KEY'] = HEX_SEC_KEY

@app.route('/')
def home():
        return render_template('index.html')

@app.route('/add_image', methods=['POST','GET'])
def add_image():
    if request.method == "POST":
        file = request.files['file']
        if file and allowed_file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print('The image file has added :', filename)
            image = cv2.imread('/home/separk/sortering/img_data/'+filename, cv2.IMREAD_UNCHANGED)
            waste = ai_image(image)
            return render_template('sorting_result.html', waste=waste)
    else:
        return('choose a proper image') 

def allowed_file(filename):
    #Add allowed file types here
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
