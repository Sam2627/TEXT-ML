import requests

request_url = "http://127.0.0.1:8000/"

data = requests.get(request_url).json()

print(data)