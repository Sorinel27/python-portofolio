from selenium import webdriver
import time

URL = "https://www.instagram.com/"
USER = "a user id"
INSTA_URL = f"https://www.instagram.com/{USER}/followers/"

email = "email@gmail.com"
password = "pass"

driver = webdriver.Chrome(executable_path="path")
driver.get(URL)

cookies = driver.find_element(by="xpath", value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
cookies.click()
time.sleep(1)
log_input = driver.find_element(by='xpath', value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
log_input.send_keys(email)
time.sleep(1)
log_input = driver.find_element(by='xpath', value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
log_input.send_keys(password)
time.sleep(1)
log_in = driver.find_element(by='xpath', value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button')
log_in.click()
time.sleep(3)

driver.get(INSTA_URL)
time.sleep(3)
number_of_people_to_follow = 100

for i in range(number_of_people_to_follow):
    follow = driver.find_element(by='xpath', value=f'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{i + 1}]/div[3]/button/div/div')
    follow.click()
    time.sleep(1)

time.sleep(10)
driver.quit()
