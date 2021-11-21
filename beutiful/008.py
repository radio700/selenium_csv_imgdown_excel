# import urllib.request
# import urllib.parse
import requests
from bs4 import BeautifulSoup as bs


url = "https://finance.naver.com/sise/lastsearch2.nhn"

source = requests.get(url)
soup = bs(source.text,"html.parser")

# for title in soup.select("a.tltle"):
#     print(title.get_text(strip=True))

for tr in soup.select("table.type_5 tr"):
    if len(tr.select("a.tltle")) == 0:
        continue
    title = tr.select("a.tltle")[0].get_text(strip=True)
    price = tr.select("td.number:nth-child(4)")[0].get_text(strip=True)
    change = tr.select("td.number:nth-child(6)")[0].get_text(strip=True)
    print(title,price,change)