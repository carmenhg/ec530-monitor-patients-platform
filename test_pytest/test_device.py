import pull_data
import push_data
import register_device
import assign_device
  

#this file contains unit tests for the device module 

#Expected Output: Succesful, should add new device to system
NotPreviouslyRegisteredJSON = {
    "device_type" : "temp",
    "device_identifier" : "MAC1"
}
def test_NotPreviouslyRegistered():
    register_device.register_device(NotPreviouslyRegisteredJSON)

#Expected Output: Unsuccessful , should notify requester
PreviouslyRegisteredJSON = {
    "device_type" : "temp",
    "device_identifier" : "MAC1"
}
def test_PreviouslyRegistered():
    register_device.register_device(PreviouslyRegisteredJSON)

#Expected Output: Unsuccessful , should notify requester
RegisteringMissingParamJSON = {
    "device_type" : "bp"
}
def test_RegisteringMissingParam():
    register_device.register_device(RegisteringMissingParamJSON)

#Expected Output: Successful ,should add device_id to users list
AssignValidJSON = {
    "device_id" : "abcd",
    "user_id" : "yupe"
}
def test_AssignValid():
    assign_device.assign_device(AssignValidJSON)

#Expected Output: Unsuccessful , should notify requester
AssignInvalidJSON = {
    "device_id" : "abcd",
    "user_id" : "ghtd"
}
def test_AssignInvalid():
    assign_device.assign_device(AssignInvalidJSON)

#Expected Output: sucessful, should display pulled data
PullDataValidDeviceJSON = {
    "device_id" : "abcd"
}
def test_PullDataValidDevice():
    pull_data.pull_data(PullDataValidDeviceJSON)

#Expected Output: Unsuccessful , should notify requester
PullDataInvalidInputSizeJSON = {
    "device_id" : "carmen",
    "user_id" : "abcd"
}
def test_PullDataInvalidInputSize():
    pull_data.pull_data(PullDataInvalidInputSizeJSON)

#Expected Output: succesful, should add new entry to measurement data json 
PushDataValidDeviceJSON = {
    "device_id" : "abcd",
    "user_id" : "yupe",
    "device_type": "temp",
    "measurement": "101",
    "timestamp" : "03/12"
}
def test_PushDataValidDevice():
    push_data.push_data(PushDataValidDeviceJSON)

#Expected Output: Unsuccessful , should notify requester
PushDataInvalidDeviceJSON = {
    "device_id" : "yo",
    "user_id" : "yupe",
    "device_type": "temp",
    "measurement": "101",
    "timestamp" : "03/12"
}
def test_PushDataInvalidDevice():
    push_data.push_data(PushDataInvalidDeviceJSON)

#Expected Output: Unsuccessful , should notify requester
PushDataInvalidUserJSON = {
    "device_id" : "abcd",
    "user_id" : "carmen",
    "device_type": "temp",
    "measurement": "101",
    "timestamp" : "03/12"
}
def test_PushDataInvalidUser():
    push_data.push_data(PushDataInvalidUserJSON)


    