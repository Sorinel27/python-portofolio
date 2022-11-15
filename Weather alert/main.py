import requests

API_KEY = "1909eb736e25a842f48193695c16d214"
# Latitude and longitude for Cluj_Napoca, RO

LAT = 46.771210
LONG = 23.623634

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
data = dict(response.json())
weather_data = data['weather']
temp_data = data['main']

print(f"The weather for {data['name']} is {weather_data[0]['main']} with a temperature of {temp_data['temp']}°C")
#to be contined...
