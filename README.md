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
This branch has only the base code for mmulti threading operations. The functions used are stub functions to test the threads operations. 


## Queue system
In order to process the text I am building a task queue system with Redis. 
Every time I submit an API request a new task or job will be added to the Redis queue for processing. 
Three main functions let me see the status of the jobs in the queue
- job.get_id(): returns the id of the newly created job after an API request 
- job.get_status(): shows me the status of a specific job while they are being processed in the queue
- job.result: shows me the result of a job, if it it finished or not (null)