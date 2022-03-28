from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import time

#Flask app initialization
app = Flask(__name__)
api = Api(app)

#celery configuration function 
from celery import Celery
def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(app)

#Here I have stub function with sleep time in between completion that act as different threads
# Add this celery decorator 
@celery.task()
def task1():
    print("Started Task 1...")
    time.sleep(6)
    print("completed .....")

@celery.task()
def task2():
    print("Started Task 2...")
    time.sleep(6)
    print("completed .....")

@celery.task()
def task3():
    print("Started Task 3...")
    time.sleep(6)
    print("completed .....")


#inside my restful call I can callthe thread module with the functions as the target. This will start a background thread while I am able to run other restful calls
class UploadMessage(Resource):
    def post(self):
        from celery_threads import task1
        task1.apply_async()

class SearchKeyword(Resource):
    def get(self):
        from celery_threads import task2
        task2.apply_async()

class RetrieveMessage(Resource):
    def get(self):
        from celery_threads import task3
        task3.apply_async()
        

api.add_resource(UploadMessage, "/send_message")
api.add_resource(SearchKeyword, "/search_keyword")
api.add_resource(RetrieveMessage, "/get_messages")

if __name__=="__main__":
    app.run(debug=True)