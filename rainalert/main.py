import requests
import os
api_key = os.environ.get("API_KEY")
parameters={
    "lat": 28.6619,
    "lon": 77.2273,
    "appid": api_key,
    "cnt":4,
}
response= requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
data=response.json()
will_rain = False
for hour_data in data["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain=True
if will_rain:
    print("Bring an umbrella")
else:
    print("No rain expected")

#environment keys= to secure api keys from hackers 
#method to do it is in terminal in caps take the name of api and key use $env:____="your_key_here" for windows
