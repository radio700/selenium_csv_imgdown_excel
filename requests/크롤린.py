import requests as req
import re

url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"

res = req.get(url)
body = res.text

#정규표현식 ==->

r = re.compile(r"h_lst.*?blind\">(.*?)</span>.*?value\">(.*?)</span>",re.DOTALL)
Cap = r.findall(body)

# print(Cap)

print("----------")
print("환율계산기")
print("----------")

for c in Cap:
    print("{0} : {1}".format(c[0],c[1]))

print()

usd = float(Cap[0][1].replace(",",""))
won = int(input("달러로 환전할 원을 입력하세야\n>>>"))
dollar = int(won/usd)
print("{0}달러로 환전됐습니다".format(dollar))

# print("{0} 현재 미국 달러".format(usd))

# print(type(usd))