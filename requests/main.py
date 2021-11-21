import requests as req

# s = '내 생일은 11월 입니다'

# bd = s.split('생일은 ')[1].split('월')[0]
# print(bd)

res = req.get("https://finance.naver.com/marketindex/?tabSel=exchange#tab_section")

# print(res.text)
html  = res.text
pos = html.find('미국 USD')
# print(pos)

s = html.split('<span class="value">')[1].split('</span>')[0]
print(s)
