from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import device


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DeviceModule.db' 
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

#Database models
#Device model: used for registering a device
class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    MAC = db.Column(db.String)
    type = db.Column(db.String)

#Device-User model: used for assigning devices to users
class DeviceUser(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    device_id= db.Column(db.Integer)

#Measurement model: used for saving device measured data for a user (patient)
class DeviceMeasurement(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer)
    device_type = db.Column(db.String)
    measurement = db.Column(db.String)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

#Schemas
#Here I can choose which values users will be able to see from the tables. 
class DeviceSchema(ma.ModelSchema):
    class Meta:
        # fields = ("id", "MAC", "type")
        model = Device
        sqla_session = db.session

device_schema = DeviceSchema()
devices_schema = DeviceSchema(many=True)

class DeviceUserSchema(ma.ModelSchema):
    class Meta:
        # fields = ("user_id", "device_id")
        model = DeviceMeasurement
        sqla_session = db.session

deviceUser_schema = DeviceUserSchema()
devicesUser_schema = DeviceUserSchema(many=True)

class DeviceMeasurementSchema(ma.ModelSchema):
    class Meta:
        # fields = ("user_id", "device_id", "device_type", "measurement", "timestamp")
        model = DeviceMeasurement
        sqla_session = db.session

deviceMeasurement_schema = DeviceMeasurementSchema()
devicesMeasurement_schema = DeviceMeasurementSchema(many=True)

# Parser will make sure that the predetremined parameters for the PUT and GET methods are met
# So all the attributes I need to call the functions will be checked before trying to push the data 
#args for getting data 
data_pull_args = reqparse.RequestParser()
data_pull_args.add_argument("device_id", type=str, help="Must provide device id")
data_pull_args.add_argument("user_id", type=str, help="Must provide user id")

#args for pushing new data 
data_push_args = reqparse.RequestParser()
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


class RegisterDevice(Resource):

    def post(self):
        args = reg_dev_args.parse_args()
        success, data = device.register_device(args["device_type"], args["device_identifier"])
        if success == True:
            return data,200
        elif success == False:
            return data
        
    
    def put(self):
        args = assign_dev_args.parse_args()
        success, data = device.assign_device(args["device_id"], args["user_id"])
        if success == True:
            return data,200
        elif success == False:
            return data

class DeviceData(Resource):

    def get(self):
        args = data_pull_args.parse_args()
        success, data = device.pull_data(args["device_id"], args["user_id"])
        if success == True:
            return data,200
        elif success == False:
            return data
    
    def post(self):
        args = data_push_args.parse_args()
        success, data = device.push_data(args["device_id"], args["user_id"], args["device_type"], args["measurement"], args["timestamp"])
        if success == True:
            return data,200
        elif success == False:
            return data

api.add_resource(RegisterDevice, "/register")
api.add_resource(DeviceData, "/data")

if __name__=="__main__":
    app.run(debug=True)
    