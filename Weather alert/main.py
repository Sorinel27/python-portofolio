import requests
from twilio.rest import Client

API_KEY = "1909eb736e25a842f48193695c16d214"  # not so secret info
# Latitude and longitude for Cluj_Napoca, RO

account_sid = 'AC75b71ff80d7412ed3f9a899bd27ddd7d'
auth_token = 'top secret info'

LAT = 46.771210
LONG = 23.623634

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
    "units": "metric"
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

client = Client(account_sid, auth_token)

# Using the free api key we can't get the weather data hourly but at 4 hours.
# This will result in the first 8 items of "list"

forecast_list = data['list']
for i in range(8):
    if forecast_list[i]['weather'][0]['id'] < 700:
        message = client.messages.create(
            body='Raining today!',
            from_='+16293483487',
            to='+40761468119'
        )
        print(message.status)
        break
