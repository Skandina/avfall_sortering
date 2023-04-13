from flask import Flask, jsonify, render_template
import mysql.connector
from mysql.connector import Error
import base64

app = Flask(__name__)

mysql_config = {
    'user': 'adminuser',
    'password': '91Djemals',
    'host': '172.31.9.67',
    'database': 'sortering'
}
@app.route('/')
def hello_world():
        return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_image():
    return ('successfully added')
    
    
@app.route('/add_image', methods=['POST'])
def upload_image():
    file = request.files['file']

   # Check if a file was provided in the request
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded'}), 400

    # Check if the file is of an allowed file type
    if not allowed_file(file.filename):
        return jsonify({'message': 'File type not allowed'}), 400

    # Convert the image data to a base64-encoded string
    image_data = base64.b64encode(file.read())

    # Save the file to the MySQL database
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(**mysql_config)

        # Create a cursor object
        cursor = conn.cursor()

        # Insert the file into the database
        cursor.execute("INSERT INTO sortering (image) VALUES (%s)", (image_data,))

        # Commit the transaction
        conn.commit()

        # Return a success message
        return jsonify({'message': 'File uploaded successfully'}), 200

    except Error as e:
        print(e)
        return jsonify({'message': 'An error occurred while uploading the file'}), 500

    finally:
        # Close the database connection
        cursor.close()
        conn.close()

def allowed_file(filename):
    # Add allowed file types here
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
