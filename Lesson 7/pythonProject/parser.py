import requests
from bs4 import  BeautifulSoup

url = "https://uaserials.pro/films/"
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")

soup_list_name = soup.find_all('div',{'class':'th-title truncate'})
for i in soup_list_name:
    print(soup)