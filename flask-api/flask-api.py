from flask import Flask
from flask_restful import Api, Resource, reqparse
import pull_data
import push_data
import register_device

app = Flask(__name__)
api = Api(app)

# Parser will make sure that the predetremined parameters for the PUT and GET methods are met
# So all the attributes I need to call the functions will be checked before trying to push the data 

#args for getting data 
data_pull_args = reqparse.RequestParser()
#the "help" parameter is essentially an error message to the sender 
data_pull_args.add_argument("device_id", type=str, help="Must provide device id", required=True)

#args for pushing new data 
data_push_args = reqparse.RequestParser()
#the "help" parameter is essentially an error message to the sender 
data_push_args.add_argument("device_id", type=str, help="Must provide device id", required=True)
data_push_args.add_argument("device_key", type=str, help="Must provide device key", required=True)
data_push_args.add_argument("device_type", type=str, help="Must provide device type", required=True)
data_push_args.add_argument("measurement", type=str, help="Must provide device measurement", required=True)
data_push_args.add_argument("timestamp", type=str, help="Must provide measurement timestamp", required=True)

#args for registering a device function 
reg_dev_args = reqparse.RequestParser()
reg_dev_args.add_argument("device_type", type=str, help="Must provide device type", required=True)
reg_dev_args.add_argument("device_key", type=str, help="Must provide device key", required=True)

class RegisterDevice(Resource):

    def post(self):
        args = reg_dev_args.parse_args()
        return register_device.register_device(args["device_type"], args["device_key"])

class DeviceData(Resource):

    def get(self):
        args = data_pull_args.parse_args()
        return pull_data.pull_data(args["device_id"])
    
    # can I define two post methods equally???
    def post(self):
        args = data_push_args.parse_args()
        return push_data.push_data(args["device_id"], args["device_key"], args["device_type"], args["measurement"], args["timestamp"])

api.add_resource(RegisterDevice, "/register")
api.add_resource(DeviceData, "/data")

if __name__=="__main__":
    app.run(debug=True)
    