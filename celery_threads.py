'''
For the python transcriber I am developing on top of "https://www.assemblyai.com/blog/deepspeech-for-dummies-a-tutorial-and-overview-part-1/" tutorial
'''

from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import time
import contextlib
import os
import wave
from deepspeech import Model
import numpy as np

############################Flask app initialization#######################################
app = Flask(__name__)
api = Api(app)

###########################celery configuration function #######################################
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



###########################Celery Task Functions#######################################
# Add the celery decorator 
@celery.task()
def transcribe():
    
    modelPath = 'models/deepspeech-0.9.3-models.pbmm'
    scorerPath = 'models/deepspeech-0.9.3-models.scorer'
    audioPath = 'audio/test_16.wav'
    
    ds = Model(modelPath)
    ds.enableExternalScorer(scorerPath)
    fin = wave.open(audioPath, 'rb')
    frames = fin.readframes(fin.getnframes())
    audio = np.frombuffer(frames, np.int16)
    text = ds.stt(audio)
    print(text)



#inside my restful call I can call the thread module with the functions as the target. This will start a background thread while I am able to run other restful calls
class Transcribe(Resource):
    def post(self):
        #this import is a workaround a bug that celery and redis have
        from celery_threads import transcribe
        transcribe.apply_async()


api.add_resource(Transcribe, "/transcribe")

if __name__=="__main__":
    app.run(debug=True)