import requests

data = {

    "title": "maksim",
    "description": "думаеm",
    "start_date": "2024-10-06",
    "end_date": "2025-04-09",
    "status": "выполнил3"
}

response = requests.post("http://127.0.0.1:8000/projects/", json=data)
print(response.status_code, response.text)