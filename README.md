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


