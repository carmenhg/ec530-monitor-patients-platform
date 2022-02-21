import requests 

Base_URL = "http://127.0.0.1:5000/"

#Unit tests for pulling data 
get_response = requests.get(Base_URL)
print(get_response.json())

#Unit tests for pushing data
post_push_response = requests.post(Base_URL, {"device_type": "temp", "device_key": "1234", "device_id": "abcdef", "measuremnet": "100", "timestamp": "16:47"})
print(post_push_response.json())

#Unit test for registering devices
#api knows which post method to call depending on args parsed???
post_register_response = requests.post(Base_URL, {"device_type": "temp", "device_key": "1234"})
print(post_register_response.json())
