#request는 그냥 웹 html을 싹다 긁어오는 역할인듯

import requests as req

url= "https://www.naver.com/"

response = req.get(url)
html = response.text
print(html)
