import register_device
import pull_data
import push_data

#this file contains unit test s for the device module 
def test1_all_data():
    device.push_data("test/device_input_data/test1.json")
    
def test2_no_did():
    device.push_data("test/device_input_data/test2.json")

def test3_pull_did_1():
    device.pull_data("1234")

def test4_pull_did_2():
    device.pull_data("abcd")
    
