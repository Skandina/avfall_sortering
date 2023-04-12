from flask import Flask, jsonify, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'my_user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'my_password'
app.config['MYSQL_DATABASE_DB'] = 'my_database'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def get():
    cur = mysql.connect().cursor()
    cur.execute('''select * from my_database.my_table''')
    r = [dict((cur.description[i][0], value)
                for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'myCollection' : r})

#@app.route("/somepage", methods=["GET","POST"])
#def some_func():
#    form_data = request.form

#    if request.method == "POST":



if __name__ == "__main__" :
    app.run(debug = True)
