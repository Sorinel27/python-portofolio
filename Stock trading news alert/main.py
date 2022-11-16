import requests
from twilio.rest import Client

STOCK = "NVDA"
COMPANY_NAME = "Nvidia"

STOCK_API_KEY = "top secret info"
NEWS_API_KEY = "top secret info"

account_sid = 'AC75b71ff80d7412ed3f9a899bd27ddd7d'
auth_token = 'top secret info'

stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
response = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
data = response.json()
last_date = data["Meta Data"]["3. Last Refreshed"]
i = 0
price_now = 0
price_past = 0
for item in data["Time Series (Daily)"]:
    if i == 2:
        break
    else:
        i += 1
        if item == last_date:
            price_now = float(data["Time Series (Daily)"][item]["4. close"])
        else:
            price_past = float(data["Time Series (Daily)"][item]["4. close"])
price_difference = price_now - price_past
price_change = (price_difference / price_past) * 100

if price_change >= 2 or price_change <= -2:
    if price_change >= 2:
        text = f"{STOCK}: 🔺{price_change}%"
    elif price_change <= 2:
        text = f"{STOCK}: 🔻{price_change}%"
    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "language": "en"
    }
    response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
    response.raise_for_status()
    data = response.json()
    articles = data["articles"]
    news_list = []

    for i in range(3):
        text += "\nHeadline: "
        text += articles[i]["title"]
        text += "\nBrief: "
        text += articles[i]["description"]

    print(text)
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=text,
        from_='+15017122661',
        to='+40761468119'
    )
