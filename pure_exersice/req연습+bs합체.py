import requests as req
from bs4 import BeautifulSoup as bs
url= "https://www.naver.com/"

response = req.get(url)

def from_url_to_html_call():
  html = response.text
  print(html)

# from_url_to_html_call()

# 진행↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#bs(html,'html.parser')
#bs(원본사이트#request.get(url)한걸 넣는다,해석기#html.parse가 대부분)

html = response.text #response.text가 html을 불러오는 메서드
soup = bs(html,"html.parser")

word = soup.select('#NM_set_home_btn')
for w in word:
  print(w.get_text(strip=False))

