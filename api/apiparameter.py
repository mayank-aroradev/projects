import requests

MY_LAT=28.6619
MY_LONG=77.2273

parameters={
    "lat":MY_LAT,
    "lng":MY_LONG,
}
response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json()
print(data)