import requests

response = requests.delete("http://127.0.0.1:8000/tasks/5/")
print(response.status_code, response.text)