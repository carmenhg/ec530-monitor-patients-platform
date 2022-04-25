from flask import Flask, url_for, request, session, redirect, render_template
from flask_restful import abort
from flask_restx import Api, Resource, reqparse
from pymongo import MongoClient
from flask_pymongo import pymongo
import device
import user_auth
import db

app = Flask(__name__)
api = Api(app)

#mongodb connection
CONNECTION_STRING = "<string>"
client = pymongo.MongoClient(CONNECTION_STRING)

#Register route
@api.route('/')
class Index(Resource):
    def index():
        if 'username' in session:
            return 'You are logged in as ' + session['username']

        return render_template('index.html')

#Register route
@api.route('/register-user')
class RegisterUser(Resource):
    
    def post(self):
        db = client.get_database('auth')
        users = pymongo.collection.Collection(db, 'users')
        login_user = users.find_one({'name' : request.form['username']})

        if login_user:
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                session['username'] = request.form['username']
                return redirect(url_for('index'))

        return 'Invalid username/password combination'
        
#Login Route 
@api.route('/login-user')
class LoginUser(Resource):
    
    def post(self):

#Logout Route 
@api.route('/logout-user')
class LogoutUser(Resource):
    
    def post(self):

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

@api.route('/register-device')
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

# api.add_resource(RegisterDevice, "/register")
# api.add_resource(DeviceData, "/data")


if __name__=="__main__":
    
    app.run()
    
