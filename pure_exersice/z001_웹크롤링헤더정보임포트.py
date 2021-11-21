import requests as req
from bs4 import BeautifulSoup as bs

header = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}

url = 'https://news.naver.com/'

res = req.get(url,headers=header)
html = res.text
soup = bs(html,"html.parser")

words = soup.select('div.hdline_news ul li .hdline_article_tit a')

for word in words:
  print(word.get_text(strip=True))