from bs4 import BeautifulSoup as bs
import requests as req
import pprint
url ="https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
resource = req.get(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
})
soup = bs(resource.text, "html.parser")

# arr = soup.select("div.name")
# for a in arr:
#     print(a.get_text(strip=False))

for desc in soup.select("div.descriptions-inner"):
    ads = desc.select("span.ad-badge")
    if len(ads) > 0:
        print("광고!")
    else:
        print(desc.select("div.name")[0].get_text(strip=True))



