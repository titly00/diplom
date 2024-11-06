import requests

response = requests.delete("http://127.0.0.1:8000/taskhistorys/4/")
print(response.status_code, response.text)
