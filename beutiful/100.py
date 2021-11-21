from typing import OrderedDict
import requests
from bs4 import BeautifulSoup
import pprint as pp
import json
from collections import OrderedDict

url= "https://finance.naver.com/marketindex/exchangeList.naver"

source = requests.get(url)
soup = BeautifulSoup(source.text,"html.parser")

file_data = OrderedDict()

list = []
# for nation in range(0,43):
for tr_lists in soup.select("div.tbl_area tbody tr:nth-child(1)"):
    for tr in tr_lists:
        list.append(tr.get_text(strip=True))
    for n in range(0,8):
        list.remove('')
# money = {
#     list[0]:{
#         "매매기준율":list[1],
#         "현찰-사실때":list[2],
#         "현찰-파실때":list[3],
#         "송금-보내실때":list[4],
#         "송금-받으실때":list[5],
#         "미화환산율":list[6],
#     }
# }
# pp.pprint(money)

file_data[list[0]] = {
    "매매기준율":list[1],
    "현찰-사실때":list[2],
    "현찰-파실때":list[3],
    "송금-보내실때":list[4],
    "송금-받으실때":list[5],
    "미화환산율":list[6],
},

with open('word.json','w',encoding="utf-8")as files:
    json.dump(file_data,files,ensure_ascii=False,indent='\t')


    # file_data["words"] = {
    #     'ram':'램',
    #     'process':'프로세스',
    #     'processor':'프로세서',
    #     'CPU':'씨피유'
    # }

# for nation in range(0,43):
# for tr_lists in soup.select("div.tbl_area tbody tr:nth-child(1)"):
#     for tr in tr_lists:
#         list.append(tr.get_text(strip=True))
#     for n in range(0,8):
#         list.remove('')
# money = {
#     list[0]:{
#         "매매기준율":list[1],
#         "현찰-사실때":list[2],
#         "현찰-파실때":list[3],
#         "송금-보내실때":list[4],
#         "송금-받으실때":list[5],
#         "미화환산율":list[6],
#     }
# }
# pp.pprint(money)



# for tr_lists in soup.select("div.tbl_area tbody tr td"):
#     print(tr_lists)
#     for tr in tr_lists:
#         list.append(tr.get_text(strip=True))
#     for n in range(0,8):
#         list.remove('')
# money = {
#     list[0]:{
#         "매매기준율":list[1],
#         "현찰-사실때":list[2],
#         "현찰-파실때":list[3],
#         "송금-보내실때":list[4],
#         "송금-받으실때":list[5],
#         "미화환산율":list[6],
#     }
# }
# pp.pprint(money)




# money = {
#     "미국":{
#         "현재가":80000,
#         "보유수량":5,
#         "매수단가": 81000,
#     },
#     "영국":{
#         "현재가":80000,
#         "보유수량":5,
#         "매수단가": 81000,
#     }
# }