from flask import Flask, render_template, url_for, request, session, redirect
import bcrypt
from flask_restx import Api
from pymongo import MongoClient
from flask_pymongo import pymongo
import device
import db

app = Flask(__name__)
api = Api(app)

#mongodb connection
CONNECTION_STRING = "mongodb+srv://carmenhg:PatalargaHG0207@cluster0.qol4e.mongodb.net/device?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
#Users collections 
db = client.get_database('auth')
users = pymongo.collection.Collection(db, 'users')
        
# @api.route('/index')
@app.route('/index')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('index.html')

# @api.route('/login')
@app.route('/login', methods=['POST'])
def login():
    login_user = users.find_one({'username' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'

# @api.route('/register')
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        existing_user = users.find_one({'username' : request.form['username']})
        print("FOUND USER")

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'username' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')

if __name__=="__main__":
    app.secret_key = 'ec530projectsecretkey'
    app.run(debug=True)