import requests

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5MjU3ODY2LCJpYXQiOjE3MjkyNTc1NjYsImp0aSI6Ijc5MDUxZTQwNzIwYzQwZDY4NDE1MDg0MjMyY2I5NzRkIiwidXNlcl9pZCI6NH0.MndkwhZ4jHhsMqsMK8Q0SpeU4bE6en6_7-0ZZE5SEuQ"
data = {
    "role": "jijij",
    "parol": 4338,
    "user": 7
}

response = requests.post("http://127.0.0.1:8000/profiles/", json=data)
print(response.status_code, response.text)