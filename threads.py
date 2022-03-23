from flask import Flask
from flask_restful import Api, Resource, reqparse
import time
import threading


app = Flask(__name__)
api = Api(app)

#Here I have stub function with sleep time in between completion that act as different threads
def task1():
    print("Started Task UploadMessage...")
    print(threading.current_thread().name)
    time.sleep(6)
    print("completed .....")

def task2():
    print("Started Task UploadMessage...")
    print(threading.current_thread().name)
    time.sleep(6)
    print("completed .....")

def task3():
    print("Started Task UploadMessage...")
    print(threading.current_thread().name)
    time.sleep(6)
    print("completed .....")

#inside my restful call I can callthe thread module with the functions as the target. This will start a background thread while I am able to run other restful calls
class UploadMessage(Resource):
    def post(self):
        threading.Thread(target=task1).start()

class SearchKeyword(Resource):
    def get(self):
        threading.Thread(target=task2).start()

class RetrieveMessage(Resource):
    def get(self):
        threading.Thread(target=task3).start()
        

api.add_resource(UploadMessage, "/send_message")
api.add_resource(SearchKeyword, "/search_keyword")
api.add_resource(RetrieveMessage, "/get_messages")

if __name__=="__main__":
    app.run(debug=True)