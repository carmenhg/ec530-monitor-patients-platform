from flask import Flask, render_template, url_for, request, session, redirect
import bcrypt
from flask_restx import Api
from pymongo import MongoClient
from flask_pymongo import pymongo
import device
import db
import os

app = Flask(__name__)
api = Api(app)
app.secret_key = os.urandom(16)

#mongodb connection
CONNECTION_STRING = "string"
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
        if request.form['pass'] == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('home'))

    return 'Invalid username/password combination'

# @api.route('/register')
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        existing_user = users.find_one({'username' : request.form['username']})

        if existing_user is None:
            users.insert_one({'username' : request.form['username'], 'password' : request.form['pass'], 'role' : request.form['role']})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/home', methods=['GET'])
def home():
    # depening on the role, screen will display different things 
    return "Home screen"
    
if __name__=="__main__":
    app.run(debug=True)
