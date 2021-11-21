import requests
from bs4 import BeautifulSoup
import pprint as pp

url= "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4817067800"

source = requests.get(url)
soup = BeautifulSoup(source.text,"html.parser")

#데이트 -> date
dt = soup.select("pubDate")
for date in dt:
    print(date.get_text(strip=True))

ah = soup.select("body>data:first-child>hour")
for aimed_hour in ah:
    print(aimed_hour.get_text(strip=True)+"시 기상정보")

#현재 날씨 ->nowweather
# for n_w in soup.select("body>data:first-child>wfEn"):
#     nowweather= n_w.get_text(strip=True)

#강수확률 
# for cr in soup.select("body>data:first-child>pop"):
#     chanse_of_rain = cr.get_text(strip=True)
# print(chanse_of_rain)

# 풍속
for ws in soup.select("body>data:first-child>ws"):
    wind_speed = ws.get_text(strip=True)
print(wind_speed)

# 습도
for hm in soup.select("body>data:first-child>reh"):
    humidity = hm.get_text(strip=True)
print(humidity)
