import requests

# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5MjU3Mjk0LCJpYXQiOjE3MjkyNTY5OTQsImp0aSI6ImU3ZjA0ZWVlMTFmMTRlOGZhNDg2Nzk0MmMzYzY1M2RiIiwidXNlcl9pZCI6M30.6kUN146V6J3eiZSs3j7ey-2r1Arm5itJtfDh73XpfXY"
data = {
    "title": "Тариэл",
    "description": "красава учиться",
    "start_date": "2024-09-11",
    "end_date": "2024-11-11",
    "status": "Новичок"
}
for i in range(3):
    print(i)
    response = requests.post('http://127.0.0.1:8000/projects/', json=data)
    print(response.status_code,response.text)
