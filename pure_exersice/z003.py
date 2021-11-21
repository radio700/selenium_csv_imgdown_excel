import requests as req
from bs4 import BeautifulSoup as bs

url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&'

params = {
  'query':'삼성전자'
}

res = req.get(url,params=params)
html = res.text

soup = bs(html,"html.parser")

words = soup.select(".news_tit")
for word in words:
  print(word.get_text(strip=True))
