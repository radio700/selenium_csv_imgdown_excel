#잘 안된다..자바스크립트로 막아둔듯.. ㅠ

import urllib.request
from bs4 import BeautifulSoup as bs
import requests as req
import pprint

url = 'https://manatoki112.net/comic/8730325'

header = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}


res = req.get(url,headers=header)

soup = bs(res.text,'html.parser')

imgUrls = soup.select("img")

count = 1
for imgUrl in imgUrls:
  down = imgUrl['src']

  opener=urllib.request.build_opener()
  opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36')]
  urllib.request.install_opener(opener)

  try:
    urllib.request.urlretrieve(down, f"{count}.jpg")
  except:
    pass
  count +=1