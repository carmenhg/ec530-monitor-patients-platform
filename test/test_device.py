# import register_device
from ... import push_data
from ... import pull_data
from ... import register_device 

#this file contains unit test s for the device module 
def test1_all_data():
    push_data.push_data("test/device_input_data/test1.json")
    
def test2_no_did():
    push_data.push_data("test/device_input_data/test2.json")

def test3_pull_did_1():
    pull_data.pull_data("1234")

def test4_pull_did_2():
    pull_data.pull_data("abcd")
    
