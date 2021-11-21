import requests
from bs4 import BeautifulSoup
import pprint as pp


url= "https://search.shopping.naver.com/search/all?query=%EA%B9%80%EC%B9%98&cat_id=&frm=NVSHATC"

source = requests.get(url)
soup = BeautifulSoup(source.text,"html.parser")

for qq in soup.select("ul.list_basis a:first-child[title]")[0]:
    print(qq.get_text(strip=True))