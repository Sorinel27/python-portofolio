import requests
import datetime

USERNAME = "sorinelboss"
TOKEN = "dibagiru7a"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "dibagiru7a",
    "username": "sorinelboss",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
'''
Create the user for pixela
'''
# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
'''
Create the graph with custom configuration
'''
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code?: "),
}

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20221103"


pixel_update_config = {
    "quantity": "5",
}
'''
Update the graph by selected day
'''
# response = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=headers)
# print(response.text)

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)
