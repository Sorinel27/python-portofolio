from bs4 import BeautifulSoup
import smtplib
import requests

shoes_data = {
    'urls': ['https://www.decathlon.ro/p/bocanci-silentiosi-si-respiranti-500-maro/_/R-p-175003?mc=8494083&c=MARO', 'https://www.buzzsneakers.ro/pantofi-sport/33228-nike-pantofi-sport-jordan-max-aura', 'https://www.escapesport.ro/jordan-max-aura-aq9084-023.html?utm_source=glami.ro&utm_medium=cpc&utm_campaign=Glami.ro&gci=c754f44588beaa64be4439b305683928dd01630b'],
    'prices': [0, 0, 0]
}

response = requests.get(shoes_data['urls'][0])
soup = BeautifulSoup(response.text, 'html.parser')
price = soup.find(name="div", class_="prc__active-price price-max-content svelte-by2p33 prc__active-price--sale")
shoes_data['prices'][0] = float(price.get("content"))

response = requests.get(shoes_data['urls'][1])
soup = BeautifulSoup(response.text, 'html.parser')
price = soup.find(name="span", class_="product-oldprice-value value").text
price = price.split(",")[0]
price = float(price)
price = price + 0.99
shoes_data['prices'][1] = price

response = requests.get(shoes_data['urls'][2])
soup = BeautifulSoup(response.text, 'html.parser')
price = soup.find(name="span", class_="fPrice -g-product-final-price-11125").text
price = price.split("\n\t\t\t")[1]
price = price.split(",")[0]
price = float(price)
shoes_data['prices'][2] = price

target_1 = 200
target_2 = 450

email_sent = False

if shoes_data['prices'][0] < target_1:
    my_email = "soringrape@gmail.com"
    my_password = "zzzz"
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.ehlo()
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="sorin78910@gmail.com",
                        msg=f"Subject:Shoes from your list are {shoes_data['prices'][0]} RON!\n\nHurry up and purchase them at this link: {shoes_data['urls'][0]}!"
                        )
    connection.close()
    email_sent = True

elif shoes_data['prices'][1] < target_2:
    my_email = "soringrape@gmail.com"
    my_password = "zzz"
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.ehlo()
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="sorin78910@gmail.com",
                        msg=f"Subject:Shoes from your list are {shoes_data['prices'][1]} RON!\n\nHurry up and purchase them at this link: {shoes_data['urls'][1]}!"
                        )
    connection.close()
    email_sent = True

elif shoes_data['prices'][2] < target_2:
    my_email = "soringrape@gmail.com"
    my_password = "zzzz"
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.ehlo()
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="sorin78910@gmail.com",
                        msg=f"Subject:Shoes from your list are {shoes_data['prices'][2]} RON!\n\nHurry up and purchase them at this link: {shoes_data['urls'][2]}!"
                        )
    connection.close()
    email_sent = True

if email_sent is False:
    my_email = "soringrape@gmail.com"
    my_password = "zzz"
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.ehlo()
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="sorin78910@gmail.com",
                        msg=f"Subject:No shoes are available for your desired price!\n\n:(\nBetter luck next time!\nPrices: {shoes_data['prices']}"
                        )
    connection.close()

# weirfhnbhgkmsuxd