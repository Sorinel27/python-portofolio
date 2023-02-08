import requests
from bs4 import BeautifulSoup
import configparser


def textToInt(text):
    if text != "Schimb" and text != "schimb":
        new_text = int(text.replace(" ", ""))
        return new_text
    return text


def main():
    # URL = input("Enter the URL: ")
    with open('url.ini', 'r+') as file:
        text = file.read()
        file.close()
    URL = text.split('\n')[0]
    keyword = text.split('\n')[1]
    URL = f'https://www.olx.ro/electronice-si-electrocasnice/telefoane-mobile/q-{keyword}/?currency=RON&search%5Border%5D=filter_float_price:asc&view=list'
    response = requests.get(URL)
    response = response.text
    soup = BeautifulSoup(response, 'html.parser')
    title = soup.title.text
    metas = soup.find_all('meta')
    description = ''
    for item in metas:
        try:
            if item.attrs['name'] == 'description':
                description = item.attrs['content']
        except:
            pass
    data_dict = {}
    print(f'{title}\n{description}')
    divs = soup.find_all(attrs={"class": "css-u2ayx9"})
    for item in divs:
        try:
            if textToInt(item.p.text.split(" lei")[0]) != "Schimb":
                data_dict[f'{item.h6.text}'] = f'{textToInt(item.p.text.split(" lei")[0])}'
        except:
            pass
    sorted_dict = sorted(data_dict.items(), key=lambda x:x[1])
    for item in sorted_dict:
        print(f'{item[0]} : {item[1]}')
# css-u2ayx9


if __name__ == '__main__':
    main()
