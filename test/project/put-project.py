import requests

data = {

    "id": 2,
    "title": "maksim",
    "description": "думаеm",
    "start_date": "2024-10-06",
    "end_date": "2025-04-09",
    "status": "выполнил3"

}

response = requests.put("http://127.0.0.1:8000/projects/10/", json=data)
print(response.status_code, response.text)
