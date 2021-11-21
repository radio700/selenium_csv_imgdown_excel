import re

# s = "color"
# print(re.match(r"colou?r",s))

s = "이 영화는 C등급입니다"
print(s.split("이 영화는")[1].split("등급")[0])
print(re.match(r"이 영화는 [ABCF\.]등급입니다",s))

print(re.findall(r"이 (..)는 ([ABCD])등급입니다",s))