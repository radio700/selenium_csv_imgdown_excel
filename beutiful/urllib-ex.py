from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

base_url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plus_url = input('검색어 입력>>')
url = base_url + quote_plus(plus_url)

# print(url)

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
img = soup.select("img._image")
for ii in soup.select("img._image"):
  print(ii.get_text(strip=True))
