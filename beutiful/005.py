import requests
from bs4 import BeautifulSoup
import pprint as pp

source = requests.get('https://www.weather.go.kr/weather/observation/currentweather.jsp')
soup = BeautifulSoup(source.text,"html.parser")


# 지역
location= []
raw_loc_list = soup.select("table.table_develop3 td>a")
for td in raw_loc_list:
    location.append(td.get_text(strip=True))
# print(location)

tempate=[]
temp = soup.select("table.table_develop3 tr td:nth-child(6)")
for tm in temp:
    tempate.append(tm.get_text(strip=True))
# print(tempate)

dic={}

for i in range(len(location)):
    dic [location[i]] = (tempate[i]+"도")

pp.pprint(dic)




