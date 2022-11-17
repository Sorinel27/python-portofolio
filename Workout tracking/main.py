"""
LINK TO SPREADSHEET: https://docs.google.com/spreadsheets/d/1YyJU1tn6a2s4HajqQWLl7eEc9u3D-BJy6fOLUAieqjM/edit#gid=0
"""
import requests
import datetime

APP_ID = "086c138e"
APP_KEY = "0472bf83304fce7dd7a36f94660cbf37"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

value = {
    "query": input("Tell me which exercises you did: "),
    "gender": "female",
    "weight_kg": 60,
    "height_cm": 180,
    "age": 21
}
print(f"You wrote: {value['query']}")

today = datetime.datetime.now()
time_now = today.strftime("%H:%M:%S")
date_now = today.strftime("%d/%m/%Y")

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", headers=headers, json=value)
data = response.json()

print(data)

for item in data['exercises']:
    sheet = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": item['name'].title(),
            "duration": item['duration_min'],
            "calories": item["nf_calories"],
        }
    }
    sheet_response = requests.post(url="https://api.sheety.co/2ea6a3db5160e5151243478f56fd811d/myWorkouts/workouts", json=sheet)
    print(sheet_response.status_code)
    print(sheet_response.text)
