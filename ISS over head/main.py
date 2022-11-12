import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 46.771210
MY_LONG = 23.623634
iss_lat = 0
iss_long = 0

def is_above():
    global iss_lat
    global iss_long
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 < iss_lat < MY_LAT + 5 and MY_LONG - 5 < iss_long < MY_LONG + 5:
        return True
    return False


def is_night():
    param = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=param)
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = time_now.hour
    if hour >= sunset or hour <= sunrise:
        return True


while True:
    if is_above():
        if is_night():
            print(f"Above you!!! The ISS lat:{iss_lat} long:{iss_long}")
            my_email = "soringrape@gmail.com"
            my_password = "zzz..."
            connection = smtplib.SMTP("smtp.gmail.com", 587)
            connection.ehlo()
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="sorin78910@gmail.com",
                                msg=f"Subject:Look Up!\n\nIt's night time and the ISS is above you!"
                                )
            connection.close()
    else:
        print(f"Not around! The ISS lat:{iss_lat} long:{iss_long}")
    time.sleep(60)
