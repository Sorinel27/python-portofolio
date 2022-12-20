from selenium import webdriver

URL = "https://orteil.dashnet.org/experiments/cookie/"

path = "your path.."
driver = webdriver.Chrome(executable_path=path)
driver.get(URL)

game_on = True
cookie = driver.find_element(by="xpath", value='//*[@id="cookie"]')


def check_item(balance, item_id, index):
    try:
        buy_element = driver.find_element(by="xpath", value=f'//*[@id="{item_id}"]/b')
        buy_element = buy_element.text.split(" ")[index]
        buy_element = buy_element.replace(",", "")
        buy_element = int(buy_element)
        if balance > buy_element:
            purchase = driver.find_element(by="xpath", value=f'//*[@id="{item_id}"]')
            purchase.click()
    except:
        pass


while game_on:
    cookie.click()
    money = driver.find_element(by="xpath", value='//*[@id="money"]')
    money = money.text.replace(",", "")
    money = int(money)
    print(money)
    # cursor
    check_item(money, "buyCursor", 2)
    # grandma
    check_item(money, "buyGrandma", 2)
    # factory
    check_item(money, "buyFactory", 2)
    # mine
    check_item(money, "buyMine", 2)
    # shipment
    check_item(money, "buyShipment", 2)
    # alchemy lab
    check_item(money, "buyAlchemy lab", 3)
    # portal
    check_item(money, "buyPortal", 2)
    # time machine
    check_item(money, "buyTime machine", 3)
driver.quit()
