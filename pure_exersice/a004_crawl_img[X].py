import urllib.request
from urllib import parse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests as req
import ssl

context = ssl._create_unverified_context()

url = 'https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q='
search = input("저장하고 싶은 사진의 검색어 입력 : ")

newUrl = url+search
resource = req.get(newUrl)
soup = BeautifulSoup(resource.text,'html.parser')

img = soup.select('img.thumb_img')
print(img)
print("실행!")

# n=1 #이름 저장할때 이름 뒤에 붙을거임
# for i in img :
#   imgUrl=i['data-source']
#   with urlopen(imgUrl) as f: #imgUrl 을 open 해서 f 에 부른다
#     with open(search + str(n) +'.jpg','wb') as h :#어떤 이름으로 저장할까 #wb = write 와 이미지이기 때문에 바이너리의 b !!
#       img = f.read()
#       h.write(img)
#   n += 1

# print('끝')