import requests

data = {

    "title": "jnih",
    "description": "думаем",
    "start_date": "2024-05-02",
    "end_date": "2025-05-09",
    "status": "выполнил"

}

response = requests.put("http://127.0.0.1:8000/projects/5/", json=data)
print(response.status_code, response.text)
