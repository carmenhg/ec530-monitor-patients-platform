import device

#this file contains unit test s for the device module 
def test1_all_data():
    device.add_data("test/device_input_data/test1.json")
    
def test2_no_did():
    device.add_data("test/device_input_data/test2.json")

def test3_pull_uid():
    device.get_data("1234", "")

def test3_pull_did():
    device.get_data("", "abcd")
    
