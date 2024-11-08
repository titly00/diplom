import requests

data = {
    'username' : 'tariel',
    'password' : '0459869'
}


response = requests.post('http://127.0.0.1:8000/users/', json=data)
print(response.status_code, response.text)