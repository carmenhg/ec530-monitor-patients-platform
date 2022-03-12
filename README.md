# ec530-monitor-patients-patform

Author: Carmen Hurtado 
## Project Description
In this project I am building a health care platform to monitor patients. The user of this platform include patients, medical professional, and system administrators. They each have different roles and access to the platform's functionalities. 

The project is divided into submodules and I am building each individually to be connected together in the final stage of development. 
The modules are:
- DEVICE
    - This module consists of an API to connect 3rd party devices (such as thermometers, scales, etc) with our system and save data to a database. 
- CHAT
    - This module has an api to manage all data sent in a chat conversation between two users. It takes care of database utilization for text, voice messages, video messages, and other attachments. 
- CALENDAR
- VOICE TRANSCRIBER
- ALERTS
- ADMINISTRATIVE
- DATA MANAGEMENT

## Branching Structure
* Each module will be implemented on their own branch
* Main will only have finalized cworking code for each moduel that will ultimately bring them all together. 

## Module Documentation
Please look at individual branches for an overall description of the module and its design. Each module will have separate files for separate functions. These files have documentation on how the interface works and specifics on how each function performs its supposed job. 
Each function will have, at the beginning of the file, a short summary of what its intended purpose is and what the data input and output look like. 

## API Methods Documentation 
Under the repo's wiki tab I will have pages that outline how each API request method works, including input and output parameters and what 3rd party users need to make use of my API. 