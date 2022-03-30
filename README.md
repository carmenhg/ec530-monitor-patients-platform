# ec530-monitor-patients-patform

Author: Carmen Hurtado 

## Design and processing criteria:

1. Simultaneous API calls: I think this would depend on the processing unit of the server
    - I am hosting my API flask app in an Azure VM. Here I can see the machine’s CPU usage over time
        - For the CPU to have a maximum efficiency for computations, we want to leave CPU usage to be a maximum of 20% at any given time. 
        - One request takes about INSERT_NUMBER_HERE percentage of CPU so we can do INSERT_NUMBER_HERE requests at a time. 
2. Different API calls procedure
    - Different APIs can run at the same time
        - The only constraint I put on this is to not have APIs that access the same database entry called at the same time
            - This can cause errors if they try to write on the same spot
            - Or if one tries to read an entry that is being modified by the other one. The information would be out of date
3. Split the processing of an API into multiple threads or processes?
    - I think Threads are better fit for this because they use share memory and we eventually want to access the same databases to manage our data 

## Organization of module 
This branch has only the base code for mmulti threading operations. The functions used are stub functions to test the threads operations. Speech to text functionality is comming soon. 


## Queue system
In order to process the text I am building an async task queue system with Celery and Redis as the broker. 
Every time I submit an API request a new task or job will be added to the queue for processing and processed. 

The code is simple, it has three functions that sleep for 6 seconds and then are finished. The functions are called from my API methods. To test the API request I am using Postman as I used for the other branches and modules of this project. 

## Celery worker 
Below we can see the multi thread queue in action through the celery worker

![Celery Worker](/images/stubs-multi-thread-celery.png)

## Flower dashboard
As a visual aid for the processing I am using Flower. Flower is a dhasboard for Celery that lets us see the tasks in the queue and other stats about the processing of the tasks. Below is an example of a connected Flower dashboard to my project where we can see that there were tasks completed by my Celery worker. 

![Celery Worker](/images/Flower-try1.png)

## Speech-to-Text 
For this functionality I am using Mozilla's DeepSpeech module. This module relies on machine learning and for that I have downloaded the training files necessary for this. These are under the models folder HOWEVER the model files are too big to commit to Github so I had to put them in my .gitignore file. But these models are being used by the transcriber and they are crucial for it to work. 
The models were downloaded from 
- [.pbmm file](https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm)
- [.scorer file](https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer)

I am using a tutorial as my 3rd party implementation of deepspeech. All code is referenced from [Here](https://lindevs.com/speech-to-text-using-deepspeech/)

The .wav files that are passed to convert to text need to have a specific format:
- sample rate: 16khz
- number of channels: 1

On mac where I was recording the audio the sample rate can only be 44khz or higher so I used *sox* to convert my .wav files to the correct sample rate. 

The model is succesful for the most part, however background noise and accent in the voice has an effect. Below we can see three different tests that returned text almost all correct. 

The first image shows an instance of a slow and less noisy audio and the results is all correct nesides my name (which I beleive my accent had a part on this). 

![Test 1](/images/speech-to-text-1.png)

The second try is an instance of a very fast talk audio. 

![Test 2](/images/speech-to-text-2.png)

The last try is an instance of an audio with more background noise. 

![Test 3](/images/speech-to-text-3.png)