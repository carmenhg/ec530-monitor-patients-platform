# Parser will make sure that the predetremined parameters for the PUT and GET methods are met
# So all the attributes I need to call the functions will be checked before trying to push the data 
#args for getting data 
data_pull_args = reqparse.RequestParser()
data_pull_args.add_argument("device_id", type=str, help="Must provide device id")
data_pull_args.add_argument("user_id", type=str, help="Must provide user id")

#args for pushing new data 
data_push_args = reqparse.RequestParser()
#device id and user id are gonna be checked against firebase not in here. 
#device id doesn't really apply here
data_push_args.add_argument("device_id", type=str, help="Must provide device id", required=True)
data_push_args.add_argument("user_id", type=str, help="Must provide user id", required=True)
data_push_args.add_argument("device_type", type=str, help="Must provide device type", required=True)
data_push_args.add_argument("measurement", type=str, help="Must provide device measurement", required=True)
data_push_args.add_argument("timestamp", type=str, help="Must provide measurement timestamp", required=True)

#args for registering a device function 
reg_dev_args = reqparse.RequestParser()
reg_dev_args.add_argument("device_type", type=str, help="Must provide device type", required=True)
reg_dev_args.add_argument("device_identifier", type=str, help="Must provide device identifier", required=True)

#args for assign a device function 
assign_dev_args = reqparse.RequestParser()
assign_dev_args.add_argument("device_id", type=str, help="Must provide device id", required=True)
assign_dev_args.add_argument("user_id", type=str, help="Must provide user id", required=True)

#Register route
@api.route('/index')
class Index(Resource):
    def get(self):
        if 'username' in session:
            return 'You are logged in as ' + session['username']

        return render_template('index.html')

#Register route
@api.route('/login')
class LoginUser(Resource):
    
    def post(self):
        db = client.get_database('auth')
        users = pymongo.collection.Collection(db, 'users')
        login_user = users.find_one({'name' : request.form['username']})

        if login_user:
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                session['username'] = request.form['username']
                return redirect(url_for('index'))

        return 'Invalid username/password combination'

@api.route('/registerdevice')
class RegisterDevice(Resource):
    @api.doc(parser=reg_dev_args)
    def post(self):
        args = reg_dev_args.parse_args()
        success, data = device.register_device(args["device_type"], args["device_identifier"])
        if success == True:
            return data,200
        elif success == False:
            return data
        
    @api.doc(parser=assign_dev_args)
    def put(self):
        args = assign_dev_args.parse_args()
        success, data = device.assign_device(args["device_id"], args["user_id"])
        if success == True:
            return data,200
        elif success == False:
            return data

@api.route('/data')
class DeviceData(Resource):
    @api.doc(parser=data_pull_args)
    def get(self):
        args = data_pull_args.parse_args()
        success, data = device.pull_data(args["device_id"], args["user_id"])
        if success == True:
            return data,200
        elif success == False:
            return data
    
    @api.doc(parser=data_push_args)
    def post(self):
        args = data_push_args.parse_args()
        success = device.push_data(args["device_id"], args["user_id"], args["device_type"], args["measurement"], args["timestamp"])
        if success == True:
            return 200
        elif success == False:
            return "Failed"

api.add_resource(RegisterDevice, "/registerdevice", endpoint = 'registerdevice')
api.add_resource(DeviceData, "/data", endpoint = 'data')
api.add_resource(Index, "/index", endpoint = 'index')
api.add_resource(LoginUser, "/login", endpoint = 'login')

##### Version with just Flask #######
from flask import Flask, render_template, url_for, request, session, redirect, flash
import bcrypt
from flask_restx import Api
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
CONNECTION_STRING = "mongodb+srv://carmenhg:PatalargaHG0207@cluster0.qol4e.mongodb.net/auth?retryWrites=true&w=majority"
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
@app.route('/index')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('index.html')

# @api.route('/login')
@app.route('/login', methods=['POST'])
def login():
    login_user = users.find_one({'username' : request.form['username']})
    current_user_role = login_user['role']

    if login_user:
        if request.form['pass'] == login_user['password']:
            session['username'] = request.form['username']
            if current_user_role == 'patient':
                return redirect(url_for('data_push'))

            if current_user_role == 'mp' or current_user_role == 'nurse':
                return redirect(url_for('assign_device'))

            if  current_user_role == 'admin':
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

@app.route('/home', methods=['GET', 'POST'])
def home():
    # register device
    if request.method == 'POST':
        existing_dev = reg_dev.find_one({'device_id' : request.form['device_id']})
        if existing_dev is None:
            reg_dev.insert_one({'device_id' : request.form['device_id'], 'device_type' : request.form['device_type']})
            return 'Success'
        else:
            return 'Device is already registered'
    return render_template('homeAdmin.html')


@app.route('/assign_patients', methods=['GET', 'POST'])
def assign_patients():
    #assign patient
    if request.method == 'POST':
        #Need to check that users are registered and their roles 
        #would be better to add a drop down menu for the available users to assign
        #that would omit the need for the check
        assign_users.insert_one({'patient': request.form['assignPatient'], 'MPs' : request.form['assignMP']})
        return 'Success'

    mps = users.find( {"role" : 'mp'}, {"username" : 1} )

    return render_template('assignPatients.html', rows=mps)
    

@app.route('/assign_device', methods=['GET', 'POST'])
def assign_device():
    #assign device
    if request.method == 'POST':
        #NEED TO ERROR CHECK THAT USER IS A PATIENT BEFORE ASSINING DOCTOR TO THEM
        #if I have drop down menus then it will basically check for me
        users.find_one_and_update({'username': request.form['assignPatient']},{ '$set': { "Devices" : request.form['assignDevice']} })
        return 'Success'

    return render_template('homeMP.html')

@app.route('/data_push', methods=['GET', 'POST'])
def data_push():
    #assign patient
    if request.method == 'POST':
        #THIS DATA NEEDS TO BE ERROR CHECKED BEFORE 
        #device and user info can be drop down menus
        #measurement and timestamp need to follow a specific format depending on device type?
        measurements.insert_one({'device_id' : request.form['device_id'], 'device_type' : request.form['device_type'], 'user_id' : request.form['user_id'], 'measurement' : request.form['measurement'], 'timestamp': request.form['timestamp']})
        return 'Success'

    return render_template('homePatient.html')
    



    