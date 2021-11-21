from bs4 import BeautifulSoup as bs
import requests as req
import pprint
url ="https://search.shopping.naver.com/search/all?cat_id=&frm=NVSHATC"

jawsparams = {
    'query':'아이폰 케이스'
}

#원래라면 url뒤에 &query=아이폰 케이스가 붙는데 따로 파라미터를 붙일 수 있다는 걸 보여주기 위해서 붙인거임
resource = req.get(url,params=jawsparams)
soup = bs(resource.text, "html.parser")

arr = soup.select("ul.list_basis div>a:first-child[title]")
for a in arr:
    pprint.pprint(a.get_text(strip=False))


