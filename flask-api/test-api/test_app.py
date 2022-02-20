import requests 

Base_URL = "http://127.0.0.1:5000/"

get_response = requests.get(Base_URL)
print(get_response.json())

#api knows which post method to call depending on args parsed???
post1_response = requests.post(Base_URL, {"device_type": "temp", "device_key": "1234"})
print(post1_response.json())

#need to add more unit tests 