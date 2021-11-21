import bs4
import requests as req
from bs4 import BeautifulSoup as bs

url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%95%84%EC%9D%B4%EC%9C%A0'

source = req.get(url)
soup = bs(source.text,"html.parser")

titles = soup.select('img._image')

for title in titles:
  print(title)
