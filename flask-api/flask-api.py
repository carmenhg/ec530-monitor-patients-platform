from flask import Flask
from flask_restful import Api, Resource, reqparse
import retrieve_message
import search_by_keyword
import upload_text_message
import upload_voice_message
import upload_video_message

app = Flask(__name__)
api = Api(app)

# Parser will make sure that the predetremined parameters for the POST and GET methods are met
# So all the attributes I need to call the functions will be checked before trying to push the data 
#the "help" parameter is essentially an error message to the sender 

#args for uploading a text message 
push_text_args = reqparse.RequestParser()
push_text_args.add_argument("sender_id", type=str, help="Must provide sender id", required=True)
push_text_args.add_argument("receiver_id", type=str, help="Must provide receiver id", required=True)
push_text_args.add_argument("data_string", type=str, help="Must provide text data", required=True)
push_text_args.add_argument("timestamp", type=str, help="Must provide timestamp", required=True)

#args for uploading a voice message
push_voice_args = reqparse.RequestParser()
push_voice_args.add_argument("sender_id", type=str, help="Must provide sender id", required=True)
push_voice_args.add_argument("receiver_id", type=str, help="Must provide receiver id", required=True)
push_voice_args.add_argument("voice", type=str, help="Must provide text data", required=True)
push_voice_args.add_argument("timestamp", type=str, help="Must provide timestamp", required=True)

#args for uploading a video message
push_video_args = reqparse.RequestParser()
push_video_args.add_argument("sender_id", type=str, help="Must provide sender id", required=True)
push_video_args.add_argument("receiver_id", type=str, help="Must provide receiver id", required=True)
push_video_args.add_argument("video", type=str, help="Must provide text data", required=True)
push_video_args.add_argument("timestamp", type=str, help="Must provide timestamp", required=True)

#args for getting messages
pull_messages_args = reqparse.RequestParser()
pull_messages_args.add_argument("receiver_id", type=str, help="Must receiver id", required=True)

#args for getting messages by keyword 
pull_keyword_args = reqparse.RequestParser()
pull_keyword_args.add_argument("receiver_id", type=str, help="Must provide receiver id", required=True)
pull_keyword_args.add_argument("keyword", type=str, help="Must provide keyword", required=True)

class UploadText(Resource):

    def post(self):
        args = push_text_args.parse_args()
        return upload_text_message.upload_text_message(args["sender_id"], args["receiver_id"], args["data_string"], args["timestamp"])

class UploadVoice(Resource):

    def pos(self):
        args = push_voice_args.parse_args()
        return upload_voice_message.upload_voice_message(args["sender_id"], args["receiver_id"], args["voice"], args["timestamp"])
    

class UploadVideo(Resource):
    def post(self):
        args = push_video_args.parse_args()
        return upload_video_message.upload_video_message(args["sender_id"], args["receiver_id"], args["video"], args["timestamp"])

class SearchKeyword(Resource):
    def get(self):
        args = pull_messages_args.parse_args()
        return search_by_keyword.search_by_keyword(args["receiver_id"], args["keyword"])

class RetrieveMessage(Resource):
    def get(self):
        args = pull_keyword_args.parse_args()
        return retrieve_message.retrieve_message(args["receiver_id"])

api.add_resource(UploadText, "/send_text")
api.add_resource(UploadVoice, "/send_voice")
api.add_resource(UploadVideo, "/send_video")
api.add_resource(SearchKeyword, "/search_keyword")
api.add_resource(RetrieveMessage, "/get_messages")

if __name__=="__main__":
    app.run(debug=True)