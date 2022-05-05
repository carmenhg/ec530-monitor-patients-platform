from flask import Flask, render_template, url_for, request, session, redirect, flash, make_response
import bcrypt
from flask_restx import Api, Resource, reqparse
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
CONNECTION_STRING = ""
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

login_parser = reqparse.RequestParser()
login_parser.add_argument('username', type=str, required=True)
login_parser.add_argument('password', type=str, required=True)
# args = parser.parse_args()
@api.route('/login')
class Login(Resource):
    @api.doc(parser=login_parser)
    def post(self):
        args = login_parser.parse_args()
        login_user = users.find_one({'username' : request.form['username']})
        
        if login_user:
            if request.form['pass'] == login_user['password']:
                session['username'] = request.form['username']
                current_user_role = login_user['role']
                session['role'] = current_user_role
                return redirect(url_for('home', role=session['role']))

        return 'Invalid username/password combination'
    
    def get(self):
        if 'username' in session:
            return make_response(render_template('home.html', role=session['role']),200,headers)
 
        else:
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template('login.html'),200,headers)

@api.route('/register')
class Register(Resource):
    def post(self):
        existing_user = users.find_one({'username' : request.form['username']})

        if existing_user is None:
            users.insert_one({'username' : request.form['username'], 'password' : request.form['pass'], 'role' : request.form['options']})
            return redirect(url_for('login'))
        
        return 'That username already exists!'
    
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('register.html'),200,headers)

@api.route('/logout')
class Logout(Resource):
    def get(self):
        session.pop('username', None)
        return redirect(url_for('login'))

@api.route('/home')
class Home(Resource):
    def get(self):
        #pull my doctors and my patients here
        patients = []
        if(request.args.get('role') == 'mp'):
            found = assign_users.find({"mp" : session['username']}, {'patient':1})
            print(found)
            for find in found:
                patients.append(find['patient'])

        mps=[]
        print(session)
        if(request.args.get('role') == 'patient'):
            found = assign_users.find({"patient" : session['username']}, {"mp":1})
            print(found)
            for find in found:
                mps.append(find['mp'])

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('home.html', user=request.args.get('role'), patients=patients, mps=mps),200,headers)

###########################################################################################

'''
This function takes in user input because it is the first step that only administrators, 
who are presumably authorized already, can do
'''
@api.route('/register_device')
class RegisterDevice(Resource):
    def post(self):
        existing_dev = reg_dev.find_one({'device_id' : request.form['device_id']})
        if existing_dev is None:
            reg_dev.insert_one({'device_id' : request.form['device_id'], 'device_type' : request.form['device_type'], "assigned": False})
            return 'Success'
        else:
            return 'Device is already registered'
    
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('registerDevice.html'),200,headers)

'''
This function has preset values that can be selected, this will limit user input and errors that come with it.
'''
@api.route('/assign_patients')
class AssignPatients(Resource):
    def post(self):
       #assign patient to mp
       #get values from user dropdown menu selction
        dropdown_values = list(request.form.values())
        mp = dropdown_values[0]
        patient = dropdown_values[1]
        assign_users.insert_one({'patient':patient, 'mp':mp})
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
'''
@api.route('/assign_device')
class AssignDevice(Resource):
    def post(self):
        #assign device
        #get values from user dropdown menu selction
        dropdown_values = list(request.form.values())
        device = dropdown_values[0]
        patient = dropdown_values[1]
        assig_dev.insert_one({'patient': patient, 'Device': device})
        reg_dev.find_one_and_update({'device_id': device},{ '$set': { "assigned" : True} })
        return 'Success'
    
    def get(self):
        devices = []
        #only devices that were not previously assigned to a patient can be assigned to a new patient
        devices_temp = reg_dev.find( {"assigned": False}, {"device_id" : 1, "device_type" : 1} )
        for device in devices_temp:
            devices.append(device['device_id'])
        
        patients = []
        patients_temp = users.find( {"role" : 'patient'}, {"username" : 1} )
        for patient in patients_temp:
            patients.append(patient['username'])

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('assignDevice.html', devices=devices, patients=patients),200,headers)

'''

'''
@api.route('/data_push')
class DataPush(Resource):
    def post(self):
        dropdown_values = list(request.form.values())
        print(dropdown_values)
        device_id = dropdown_values[0].partition(":")[2]
        device_type = dropdown_values[0].partition(":")[0]
        patient = dropdown_values[1]
        measurements.insert_one({'device_id' : device_id, 'device_type' : device_type, 'user_id' : patient, 'measurement' : request.form['measurement'], 'timestamp': request.form['timestamp']})
        return 'Success'

    def get(self):

        devices = []
        devices_type = []
        if(session['role'] == 'mp'):
            #only devices that are assigned to a patient can add data
            devices_temp = reg_dev.find( {"assigned": True}, {"device_id" : 1, "device_type" : 1} )
            for device in devices_temp:
                devices.append(device['device_type'] + ': ' +device['device_id'])

        #different devices list if the user is a patient
        #only devices that are assigned to a patient can add data
        if(session['role'] == 'patient'):
            devices_temp = assig_dev.find( {"patient": session['username']}, {"Device" : 1} )
            for device in devices_temp:
                devices.append(device['Device'] + ': Unknown')

        patients = []
        patients_temp = assig_dev.find({})
        for patient in patients_temp:
            if patient['patient'] not in patients:
                patients.append(patient['patient'])
        

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('dataPush.html', devices=devices, patients=patients, role=session['role']),200,headers)

'''
Delete methods
'''
@api.route('/unassign_patients')
class UnassignPatients(Resource):  
    def get(self):
        return

    def delete(self):
        return

@api.route('/unassign_devices')
class UnassignDevices(Resource):  
    def get(self):
        return

    def delete(self):
        return

@api.route('/delete_devices')
class DeleteDevices(Resource):  
    def get(self):
        return

    def delete(self):
        return

if __name__=="__main__":
    app.run(debug=True)
