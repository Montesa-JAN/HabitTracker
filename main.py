import requests
from datetime import datetime

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "Coding Graph",
    "unit": "Hrs",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

post_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPHID}"

today_date = datetime.now()

post_config = {
    "date": today_date.strftime("%Y%m%d"),
    "quantity": input("How many hours did you study today?"),
}

response = requests.post(url=post_endpoint, json=post_config, headers=headers)

pixela_update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPHID}/{today_date.strftime('%Y%m%d')}"

update_pixel_data = {
    "quantity": "5"
}

# response = requests.put(url=pixela_update_endpoint, json=update_pixel_data, headers=headers)

pixela_delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPHID}/{today_date.strftime('%Y%m%d')}"

# response = requests.delete(url=pixela_delete_endpoint, headers=headers)
