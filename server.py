import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import mysql.connector
from mysql.connector import Error
import secret 

app = Flask(__name__)

UPLOAD_FOLDER = '/home/ubuntu/image_data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

HEX_SEC_KEY = secret.secret_key()
app.config['SECRET_KEY'] = HEX_SEC_KEY

app.config['MYSQL_HOST'] = '16.170.167.121'
app.config['MYSQL_USER'] = 'adminuser'
app.config['MYSQL_PASSWORD'] = '91Djemals'
app.config['MYSQL_DB'] = 'sortering'

@app.route('/')
def home():
        return render_template('index.html')
@app.route('/test')
def test():
    return render_template('upload_image.html')

@app.route('/add_image', methods=['POST','GET'])
def add_image():
    if request.method == "POST":
        file = request.files['file']
        if file and allowed_file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print('hahaha')
            return ('successfully uploaded')
        else:
            return flash('choose a proper image') 

def allowed_file(filename):
    #Add allowed file types here
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
