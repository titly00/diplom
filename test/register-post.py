import requests

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxMDY3MjY3LCJpYXQiOjE3MzEwNjY5NjcsImp0aSI6ImNlZDFmZDNhYjgwMDQ3YzliMTAxMWQwYmZlNzgwZjNmIiwidXNlcl9pZCI6N30.NxaopFHT06hqCixBL6kEL1JG1B2hbX28vyV2sXVC5cc"


data = {
    "user": 9 ,
    "name": "Arietyi",
    "robot": "read code",
    "register": "site"

}


response = requests.post('http://127.0.0.1:8000/register/', json=data)
print(response.status_code, response.text)