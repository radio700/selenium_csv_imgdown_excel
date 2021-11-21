from bs4 import BeautifulSoup as bs
import requests as req

url = "https://finance.naver.com/marketindex/exchangeList.nhn"
res = req.get(url)
soup = bs(res.text, "html.parser")

tds = soup.find_all("td")
# print(tds)


names = []
for td in tds:
    if len(td.find_all("a")) == 0:
        continue
    names.append(td.get_text(strip=True))

price= []
for td in tds:
    if "sale" in td.attr:
        if "sale" in td.attr("class"):
            price.append(td.get_text(strip=True))

print("names")
price("price")
