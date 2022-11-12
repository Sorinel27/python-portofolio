import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get('https://opentdb.com/api.php', params=parameters)
response.raise_for_status()
q_data = response.json()
data = q_data['results']
