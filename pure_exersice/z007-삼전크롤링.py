import requests as req
from bs4 import BeautifulSoup as bs

#https://www.youtube.com/watch?v=n8_SeIZ_vo4&t=5s

#종목 code list
codes = {
  '005930':'삼성전자',
  '000660':'sk하이닉스',
  '035720':'kakao',
}

for code in codes:

  url = f"https://finance.naver.com/item/sise.naver?code={code}"

  type = codes[f'{code}']
  print(f'{type}입니다')

  res = req.get(url)
  html = res.text
  soup = bs(html,'html.parser')

  costs = soup.select('#_nowVal')

  for cost in costs:
    print(cost.get_text(strip=True))
    print()
