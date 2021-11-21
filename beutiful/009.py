from bs4.builder import TreeBuilder
import requests as req
from bs4 import BeautifulSoup as bs
import pprint


url = "https://finance.yahoo.com/cryptocurrencies"

res = req.get(url)
soup = bs(res.text,"html.parser")

for tr in soup.select("table tbody tr"):
  # pprint.pprint(tr.get_text(strip=True))
  title = tr.select("td:nth-child(1) a")[0].get_text(strip=True)
  price = tr.select("td:nth-child(3) span")[0].get_text(strip=True)
  # change = tr.select("td:nth-child(5) span")[0].get_text(strip=True)
  print(title,price)
