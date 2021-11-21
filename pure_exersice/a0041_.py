import requests as req
from bs4 import BeautifulSoup
import ssl

context = ssl._create_unverified_context()
url = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
html = req.get(url)
soup = BeautifulSoup(html.text,'html.parser')

titles = soup.select('ul.lst_total a.total_tit')
for title in titles:

  print(title.get_text(strip=True))
  print(title.attrs['href'])
  print("\n")
