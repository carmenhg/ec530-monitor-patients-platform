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
Below is an image of the celery worker started. We can see how the tasks are queued and processed. The print statements I added inside the functions code to track in the celery worker's console. 

![Celery Worker](/images/celery-worker-started.png)

In the next image we can see the multi thread queue in action through the celery worker

![Celery Worker](/images/stubs-multi-threads-celery.png)

## Flower dashboard
As a visual aid for the processing I am using Flower. Flower is a dhasboard for Celery that lets us see the tasks in the queue and other stats about the processing of the tasks. Below is an example of a connected Flower dashboard to my project where we can see that there were tasks completed by my Celery worker. 

![Celery Worker](/images/Flower-try1.png)