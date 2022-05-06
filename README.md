# ec530-monitor-patients-patform

Author: Carmen Hurtado 
## Project Description

## Final Project Information
**This repo serves for both project 2 and final project for this class. TO SEE FINAL VERSION OF THE FINAL PROJECT PLEASE GO TO THE "DEVICE" BRANCH**

## Project 2 Information
**Please visit the wiki page for this repo for a more detailed documentation on each API function for the different modules that are implemented [WIKI](https://github.com/carmenhg/ec530-monitor-patients-platform/wiki/Chat-Module)**
In this project I am building a health care platform to monitor patients. The user of this platform include patients, medical professional, and system administrators. They each have different roles and access to the platform's functionalities. 

The project is divided into submodules and I am building each individually to be connected together in the final stage of development. 
The modules are:
- DEVICE
    - This module consists of an API to connect 3rd party devices (such as thermometers, scales, etc) with our system and save data to a database. 
- CHAT
    - This module has an api to manage all data sent in a chat conversation between two users. It takes care of database utilization for text, voice messages, video messages, and other attachments. 
- CALENDAR
- VOICE TRANSCRIBER
    - This module utilizes multi threading oprations to achive this. The code is under banch named threads.
- ALERTS
- ADMINISTRATIVE
- DATA MANAGEMENT

### Branching Structure
* Each module will be implemented on their own branch. Main reason to do this is to build modularity and have each module not be dependent of the other. 
* **For the final project I will finalize the application that will utilize these modules and then all this cocde will come together. For now please look at individual branches**


### Module Documentation
Please look at individual branches for an overall description of the module and its design. Each module will have separate files for separate functions. These files have documentation on how the interface works and specifics on how each function performs its supposed job. 
Each function will have, at the beginning of the file, a short summary of what its intended purpose is and what the data input and output look like. 

### API Methods Documentation 
Under the repo's wiki tab I will have pages that outline how each API request method works, including input and output parameters and what 3rd party users need to make use of my API. 