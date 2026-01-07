import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "hjj8u84373buyh3ruh"
USERNAME = "mallu"
GRAPH_ID="graph25071"
user_params = {

"token": TOKEN,
"username": USERNAME,
"agreeTermsOfService": "yes",
"notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_params = {
    "id": GRAPH_ID,
    "name": "Habit Tracker",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu"
}
headers = {
    "x-user-token": TOKEN}
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs" 
# reqit=requests.post(url=graph_endpoint, json=graph_params, headers={"X-USER-TOKEN": TOKEN})
# print(reqit.text)
today=datetime(year=2020, month=1, day=1)


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
picel_data = {
    "date": today.strftime("%Y%m%d"),

    "quantity": "30"

}
# responsed=requests.post(url=pixel_creation_endpoint, json=picel_data, headers=headers)
# print(responsed.text)

put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
put_data = {
    "quantity": "45"
}
reponse= requests.put(url=put_endpoint, json=put_data, headers=headers)
print(reponse.text)