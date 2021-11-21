import feedparser

url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4817067800"

feedparser.parse(url)
