import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
import requests

# airbnb_url = "http://shorturl.at/ekBLO"
airbnb_url = 'https://www.airbnb.com/s/Los-Angeles/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&date_picker_type=flexible_dates&adults=4&source=structured_search_input_header&search_type=search_query&room_types%5B%5D=Entire%20home%2Fapt'
response = requests.get(airbnb_url)
response = response.text
soup = BeautifulSoup(response, 'html.parser')

divs = []
links = []
prices = []
dates = []

for item in soup.find_all('div', 'c4mnd7m dir dir-ltr'):
    divs.append(item)

reference = 0
for item in divs:
    for tag in item.find_all('meta'):
        if tag['itemprop'] == 'url':
            links.append(tag['content'])
    for tag in item.find_all('span', 'a8jt5op dir dir-ltr'):
        if tag.string.split(' ')[1] == 'total':
            prices.append(tag.string.replace('\xa0', ' '))
    for tag in item.find_all('span', 'dir dir-ltr'):
        reference += 1
        if reference % 3 == 0:
            dates.append(tag.string)

# print(f'links: {links}\nprices: {prices}\ndates: {dates}')

forms_url = "https://forms.gle/EkdMcxKcJS1LKqRG9"
selenium_path = "...driver path"
service = Service(selenium_path)
driver = webdriver.Chrome(service=service)

for i in range(len(links)):
    driver.get(forms_url)
    time.sleep(1)
    field = driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]')
    field.send_keys(dates[i])
    field = driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]')
    field.send_keys(prices[i])
    field = driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]')
    field.send_keys(links[i])
    send = driver.find_element(by='xpath', value='/html/body/div/div[3]/form/div[2]/div/div[3]/div[1]/div[1]/div/span')
    send.click()

driver.quit()
