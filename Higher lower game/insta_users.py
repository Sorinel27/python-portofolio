import urllib.request
from bs4 import BeautifulSoup

print("Loading the users followers...")

fp = urllib.request.urlopen("https://en.wikipedia.org/wiki/List_of_most-followed_Instagram_accounts")
myBytes = fp.read()

url = myBytes.decode("utf8")
fp.close()
soup = BeautifulSoup(url, "html.parser")

urls = []
insta_urls = []

for link in soup.find_all('a'):
    urls.append(link.get('href'))
for i in urls:
    if i is not None:
        for j in range(len(i)):
            if (i[j] == 'm' and j == 20) and i[0] == 'h':
                insta_urls.append(i)
a = 0
users = []
for user in insta_urls:
    users.append(user[26: len(user) + 1])
