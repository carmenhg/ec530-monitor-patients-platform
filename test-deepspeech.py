import wave
from deepspeech import Model
import numpy as np

def transcribe():
    
    modelPath = 'models/deepspeech-0.9.3-models.pbmm'
    scorerPath = 'models/deepspeech-0.9.3-models.scorer'
    audioPath = 'audio/test.wav'
    
    ds = Model(modelPath)
    ds.enableExternalScorer(scorerPath)
    fin = wave.open(audioPath, 'rb')
    frames = fin.readframes(fin.getnframes())
    audio = np.frombuffer(frames, np.int16)
    text = ds.stt(audio)
    print("Before text")
    print(text)

if __name__=="__main__":
    transcribe()