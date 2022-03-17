from flask import Flask
from flask_restful import Api, Resource, reqparse
import retrieve_message
import search_by_keyword
import upload_message


app = Flask(__name__)
api = Api(app)

# Parser will make sure that the predetremined parameters for the POST and GET methods are met
# So all the attributes I need to call the functions will be checked before trying to push the data 
#the "help" parameter is essentially an error message to the sender 

#args for uploading a message 
push_args = reqparse.RequestParser()
push_args.add_argument("sender_id", type=str, help="Must provide sender id", required=True)
push_args.add_argument("receiver_id", type=str, help="Must provide receiver id", required=True)
push_args.add_argument("data_string", type=str, help="Must provide text data", required=True)
push_args.add_argument("data_voice", type=str, help="Must provide text data")
push_args.add_argument("data_video", type=str, help="Must provide text data")
push_args.add_argument("timestamp", type=str, help="Must provide timestamp", required=True)

#args for getting messages
pull_messages_args = reqparse.RequestParser()
pull_messages_args.add_argument("receiver_id", type=str, help="Must receiver id", required=True)

#args for getting messages by keyword 
pull_keyword_args = reqparse.RequestParser()
pull_keyword_args.add_argument("receiver_id", type=str, help="Must provide receiver id", required=True)
pull_keyword_args.add_argument("keyword", type=str, help="Must provide keyword", required=True)

class UploadMessage(Resource):

    def post(self):
        args = push_args.parse_args()
        success, data = upload_message.upload_message(args["sender_id"], args["receiver_id"], args["data_string"], args["data_voice"], args["data_video"], args["timestamp"])
        if success == True:
            return data,200
        elif success == False:
            return data, 400 

class SearchKeyword(Resource):
    def get(self):
        args = pull_keyword_args.parse_args()
        success, data = search_by_keyword.search_by_keyword(args["receiver_id"], args["keyword"])
        if success == True:
            return data,200
        elif success == False:
            return data, 400

class RetrieveMessage(Resource):
    def get(self):
        args = pull_messages_args.parse_args()
        success, data = retrieve_message.retrieve_message(args["receiver_id"])
        if success == True:
            return data,200
        elif success == False:
            return data, 400

api.add_resource(UploadMessage, "/send_message")
api.add_resource(SearchKeyword, "/search_keyword")
api.add_resource(RetrieveMessage, "/get_messages")

if __name__=="__main__":
    app.run(debug=True)