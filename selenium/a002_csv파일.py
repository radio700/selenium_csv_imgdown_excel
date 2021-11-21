from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys #엔터칠때 필요
import csv

#밑에 두줄은 환경세팅
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

#브라우저생성
browser = webdriver.Chrome('C:\chromedriver.exe',options=options)
browser.implicitly_wait(15) # 묵시적 대기, 활성화를 최대 15초가지 기다린다.

# 1)페이지 가져오기(이동)
browser.get('https://www.naver.com')


# 2)페이지 이동
time.sleep(1)
browser.find_element_by_css_selector('a.nav.shop').click()

# 3)쇼핑검색창 클릭
search = browser.find_element_by_css_selector('.co_srh_input')
search.click()

# 4)검색어 입력
search.send_keys("아이폰 13")
search.send_keys(Keys.ENTER)


# 스크롤 전 높이
before_h = browser.execute_script('return window.scrollY')
# [execute_script]는 현재 스크롤된 높이 메쏘드는 JS를 실행하는 것

# 5)무한베기

for i in range(5):

  # 맨 아래로 스크롤 함
  after_h = browser.find_element_by_css_selector("body").send_keys(Keys.END)#엔드키 존나눌러
  time.sleep(0.5)

# 파일생성
f = open(r"C:\Users\jaws\Desktop\crwal\project\selenium\data.csv",'w',encoding='cp949', newline='')
csvwriter = csv.writer(f)



# 상품정보 div
items = browser.find_elements_by_css_selector(".basicList_info_area__17Xyo")#element[s]주의

for item in items:
  name = item.find_element_by_css_selector(".basicList_title__3P9Q7").text
  prices = item.find_element_by_css_selector(".price_num__2WUXn").text
  price = int(prices.replace("원","").replace(",",""))
  link = item.find_element_by_css_selector(".basicList_title__3P9Q7 > a").get_attribute('href')
  print(name,price)
  #데이터쓰기
  csvwriter.writerow([name,price,link])

f.close()
  






# 5초후 종료
time.sleep(36000)
browser.quit() # 웹 브라우저 종료. browser.close()는 탭 종료