import requests
response = requests.get('http://127.0.0.1:8000/taskhistorys/4/')

if response.status_code == 200:
    users = response.json()
    print(users)