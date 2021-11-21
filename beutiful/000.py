from bs4 import BeautifulSoup as bs
import requests as req
import pprint

url ="https://search.shopping.naver.com/search/all?query=%EC%95%84%EC%9D%B4%ED%8F%B0+%EC%BC%80%EC%9D%B4%EC%8A%A4&cat_id=&frm=NVSHATC"


resource = req.get(url)
soup = bs(resource.text, "html.parser")

arr = soup.select("ul.list_basis div>a:first-child[title]")

for a in arr:
    pprint.pprint(a.get_text(strip=False))


