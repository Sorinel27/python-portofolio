from selenium import webdriver
import time


SPEED_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/i/flow/login"

path = "your path"

driver = webdriver.Chrome(executable_path=path)
driver.get(SPEED_URL)

speed_cookie_xpath = driver.find_element(by="xpath", value='//*[@id="onetrust-accept-btn-handler"]')
speed_cookie_xpath.click()
time.sleep(3)

speed_go_xpath = driver.find_element(by="xpath", value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
speed_go_xpath.click()

time.sleep(60)

d_speed = driver.find_element(by="xpath", value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
d_speed = d_speed.text
print(d_speed)

u_speed = driver.find_element(by="xpath", value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
u_speed = u_speed.text
print(u_speed)

username = "Sorin63701900"
password = "carsorin"

driver.get(TWITTER_URL)

time.sleep(3)
user_input_xpath = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label')
user_input_xpath.send_keys(username)
next_button = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
next_button.click()
time.sleep(5)
password_input_xpath = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password_input_xpath.send_keys(password)
log_in = driver.find_element(by="xpath", value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
log_in.click()
time.sleep(5)


tweet = driver.find_element(by="xpath", value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
tweet.click()

post_tweet = driver.find_element(by="xpath", value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
message = f"According to Speedtest by Ookla, I have the following:\nDownload: {d_speed}\nUpload: {u_speed}"
post_tweet.send_keys(message)

tweet = driver.find_element(by="xpath", value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
tweet.click()


driver.quit()