import requests 

Base_URL = "http://127.0.0.1:5000/"

#Unit tests for pushing data
post_push_response = requests.post(Base_URL + "data", {"device_type": "temp", "device_key": "test1", "device_id": "abcd", "measurement": "100", "timestamp": "16:47"})
print(post_push_response.json())

#Unit tests for pulling data 
get_response = requests.get(Base_URL + "data", {"device_id": "abcd"})
print(get_response.json())

#Unit test for registering devices
post_register_response = requests.post(Base_URL + "register", {"device_type": "temp", "device_key": "hellocarmen2"})
print(post_register_response.json())
