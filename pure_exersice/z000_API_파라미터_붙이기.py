import requests as req

url = 'https://section.blog.naver.com/Search/Post.nhn?pageNo=1&rangeType=ALL&orderBy=sim&keyword=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

params = {
    'pageNo' : 1,
    'rangeType' : 'ALL',
    'orderBy' : 'sim',
    'keyword' : '파이썬'
}

response = req.get('https://section.blog.naver.com/Search/Post.nhn', params=params)
#get 방식으로 파라미터를 붙인다
print(response.status_code)
print(response.url)