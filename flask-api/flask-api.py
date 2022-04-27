from flask import Flask, render_template, url_for, request, session, redirect, flash, make_response
import bcrypt
from flask_restx import Api, Resource
from pymongo import MongoClient
from flask_pymongo import pymongo
import device
import db
import os
import random

app = Flask(__name__)
api = Api(app)
app.secret_key = os.urandom(16)

#mongodb connection
CONNECTION_STRING = "string"
client = pymongo.MongoClient(CONNECTION_STRING)
#Users collections 
db_users = client.get_database('auth')
users = pymongo.collection.Collection(db_users, 'users')
assign_users = pymongo.collection.Collection(db_users, 'assigned')

#Device collections 
db_device = client.get_database('device')
reg_dev = pymongo.collection.Collection(db_device, 'registered')
assig_dev = pymongo.collection.Collection(db_device, 'assigned')
measurements = pymongo.collection.Collection(db_device, 'measurements')
        
@api.route('/index')
class Index(Resource):
    def get(self):
        if 'username' in session:
            return 'You are logged in as ' + session['username']
        else:
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template('index.html'),200,headers)

@api.route('/login')
class Login(Resource):
    def post(self):
        login_user = users.find_one({'username' : request.form['username']})
        current_user_role = login_user['role']

        if login_user:
            if request.form['pass'] == login_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for('home', role=current_user_role))
                # if current_user_role == 'patient':
                #     return redirect(url_for('data_push'))

                # if current_user_role == 'mp' or current_user_role == 'nurse':
                #     return redirect(url_for('assign_device'))

                # if  current_user_role == 'admin':
                #     return redirect(url_for('home'))

        return 'Invalid username/password combination'

@api.route('/register')
class Register(Resource):
    def post(self):
        existing_user = users.find_one({'username' : request.form['username']})

        if existing_user is None:
            users.insert_one({'username' : request.form['username'], 'password' : request.form['pass'], 'role' : request.form['role']})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'
    
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('register.html'),200,headers)

@api.route('/logout')
class Logout(Resource):
    def get(self):
        session.pop('username', None)
        return redirect(url_for('index'))

@api.route('/home')
class Home(Resource):
    
    def get(self):
        # login_user = users.find_one({'username' : request.form['username']})
        # current_user_role = login_user['role']
        # user = session["username"]
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('home.html', user=request.args.get('role')),200,headers)

'''
This function takes in user input because it is the first step that only administrators, 
who are presumably authorized already, can do
'''
@api.route('/register_device')
class RegisterDevice(Resource):
    def post(self):
        # register device
        existing_dev = reg_dev.find_one({'device_id' : request.form['device_id']})
        if existing_dev is None:
            reg_dev.insert_one({'device_id' : request.form['device_id'], 'device_type' : request.form['device_type']})
            return 'Success'
        else:
            return 'Device is already registered'
    
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('homeAdmin.html'),200,headers)

'''
This function has preset values that can be selected, this will limit user input and errors that come with it.
'''
@api.route('/assign_patients')
class AssignPatients(Resource):
    def post(self):
       #assign patient to mp
        dropdown_values = list(request.form.values())
        mp = dropdown_values[0]
        patient = dropdown_values[1]
        assign_users.insert_one({'patient': patient, 'MPs' : mp})
        return 'Success'

    def get(self):
        mps = []
        mps_temp = users.find( {"role" : 'mp'}, {"username" : 1} )
        for mp in mps_temp:
            mps.append(mp['username'])

        patients = []
        patients_temp = users.find( {"role" : 'patient'}, {"username" : 1} )
        for patient in patients_temp:
            patients.append(patient['username'])

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('assignPatients.html', mps=mps, patients=patients),200,headers)
    
'''
This function has preset values that can be selected, this will limit user input and errors that come with it.
STILL LEFT TO IMPLEMENT 
'''
@api.route('/assign_device')
class AssignDevice(Resource):
    def post(self):
        #assign device
        users.find_one_and_update({'username': request.form['assignPatient']},{ '$set': { "Devices" : request.form['assignDevice']} })
        return 'Success'
    
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('homeMP.html'),200,headers)

@api.route('/data_push')
class DataPush(Resource):
    def post(self):
        measurements.insert_one({'device_id' : request.form['device_id'], 'device_type' : request.form['device_type'], 'user_id' : request.form['user_id'], 'measurement' : request.form['measurement'], 'timestamp': request.form['timestamp']})
        return 'Success'

    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('homePatient.html'),200,headers)
    
if __name__=="__main__":
    app.run(debug=True)
