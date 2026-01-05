import requests
api_key = "f44a758757100ac23e882daf2974ffd1"
parameters={
    "lat": 28.6619,
    "lon": 77.2273,
    "appid": api_key,
}
response= requests.get("https://api.openweathermap.org/data/2.5/onecall",params=parameters)
print(response.status_code)