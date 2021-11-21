import requests as req
from bs4 import BeautifulSoup as bs
import pyautogui
#https://www.youtube.com/watch?v=n8_SeIZ_vo4&t=5s
key = pyautogui.prompt("검색어입력>>>")

url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='+key

res = req.get(url)
html = res.text

soup = bs(html,"html.parser")

words = soup.select(".news_tit")

for word in words:
  title = word.text
  url = word.attrs['href']
  print(title,url)
