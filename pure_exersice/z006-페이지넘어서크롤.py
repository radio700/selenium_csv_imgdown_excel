import requests as req
from bs4 import BeautifulSoup as bs
import pyautogui

#https://www.youtube.com/watch?v=n8_SeIZ_vo4&t=5s

key = pyautogui.prompt("검색어입력>>>")
lastpage = int(pyautogui.prompt("몇페이지까지 할까요?"))

page_num = 1
for page_query in range(1,lastpage*10,10):
  print(f'{page_num}페이지 입니다======================================================')
  url = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={key}&start={page_query}'

  res = req.get(url)
  html = res.text

  soup = bs(html,"html.parser")

  words = soup.select(".news_tit")

  for word in words:
    title = word.text
    url = word.attrs['href']
    print(title,url)
  page_num +=1
