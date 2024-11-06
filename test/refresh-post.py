import requests

token =  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMDU1NTYwMywiaWF0IjoxNzMwNDY5MjAzLCJqdGkiOiI0NDA0YTEwMjU3YTY0ODYxYmRkZThjYzNlOTlmMjA5YyIsInVzZXJfaWQiOjd9.ZJ42oCljxr5LXeYZMN26NFYS_MFo5AI-MnpFgpIHfwA",

data = {
    "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMDU1NTYwMywiaWF0IjoxNzMwNDY5MjAzLCJqdGkiOiI0NDA0YTEwMjU3YTY0ODYxYmRkZThjYzNlOTlmMjA5YyIsInVzZXJfaWQiOjd9.ZJ42oCljxr5LXeYZMN26NFYS_MFo5AI-MnpFgpIHfwA"
}

response = requests.post("http://127.0.0.1:8000/api/token/refresh/", json=data)
print(response.status_code, response.text)

