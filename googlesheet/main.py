import requests
import datetime as dt
    

APP_ID = "app_4b0c6257773942b695551c2a"
APP_KEY = "nix_live_JaAVvdMe9DRB1o15hLSDwH4VBkuiYC14"
SHEET_NAME = "Daily Expenses"
GENDER = "male"
AGE = 18
HEIGHT_CM = 175
WEIGHT_KG = 70

exercise_text = input("Tell me which exercise you did: ").strip()



sheet_endpoint = "https://api.sheety.co/e43e87fa730695aca4488c5d9147b583/untitledSpreadsheet/sheet1"
Base_URL="https://app.100daysofpython.dev"

calorie_endpoint=f"https://trackapi.nutritionix.com/v2/natural/exercise"

headers={
    "x-app-id":APP_ID,
    "x-app-key":APP_KEY,
    "Content-Type":"application/json"
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# response=requests.post(url=calorie_endpoint,json=data,headers=headers)
# result=response.json()
response=requests.post(url=calorie_endpoint,json=parameters,headers=headers)
result=response.json()
print(result)

today_timee=dt.datetime.now().strftime("%d/%m/%Y")
now_time=dt.datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_timee,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)
    print(sheet_response.text)