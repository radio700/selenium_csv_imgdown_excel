import requests as req
from bs4 import BeautifulSoup as bs

url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90'

res = req.get(url)
html = res.text

soup = bs(html,"html.parser")

words = soup.select(".news_tit")
for word in words:
  print(word.get_text(strip=True))
