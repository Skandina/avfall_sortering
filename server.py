import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import mysql.connector
from mysql.connector import Error
import secret 
from app import ai_image
from chatapp import chat_answer
import cv2
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = '/home/separk/sortering/img_temp/'
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
            extension = os.path.splitext(filename)[1]
            changed_name = os.path.splitext(filename)[0]

            if extension == '.png':
                image = Image.open(UPLOAD_FOLDER+filename).convert('RGB')
                image.save(UPLOAD_FOLDER+changed_name+'.jpg', 'jpeg')
                image = Image.open(UPLOAD_FOLDER+changed_name+'.jpg')
                print("image path :")
                print("The image has saved") 
                waste = ai_image(image)

            else : 
                image = cv2.imread('/home/separk/sortering/img_temp/'+filename, cv2.IMREAD_UNCHANGED) 
                waste = ai_image(image)
                
            chat_result = chat_answer(waste)
            file = open("tmp.txt", "w")
            file.write(chat_result)
            file.close()
            chat_file = open("tmp.txt", "r")
            chat_text = chat_file.read()
            chat = chat_text.replace('\n', '<br>')

            return render_template('sorting_result.html', waste=waste, chat=chat)
    else:
        return('choose a proper image') 

def allowed_file(filename):
    #Add allowed file types here
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
