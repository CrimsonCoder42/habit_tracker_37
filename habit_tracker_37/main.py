import requests
import datetime


USERNAME = "devin3737"
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "www8675309"
GRAPHID = "graph1"
TODAY = datetime.datetime.now().strftime("%Y%m%d")

user_params = {
    "token": "www8675309",
    "username": "devin3737",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ichou"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

add_pixel_config = {
    "date": TODAY,
    "quantity": "5.0",

}

# response = requests.post(url=add_pixel_endpoint, json=add_pixel_config, headers=headers)
# print(response.text)

update_pixel_config = {
    "quantity": "3.0",

}

update_pixel_endpoint = f"{add_pixel_endpoint}/{TODAY}"

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

# Delete Pixel
delete_pixel_endpoint = f"{add_pixel_endpoint}/{TODAY}"

response = requests.delete(url=delete_pixel_endpoint, json=update_pixel_config, headers=headers)
print(response.text)
