from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys #엔터칠때 필요

#밑에 두줄은 환경세팅
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])



#브라우저생성
browser = webdriver.Chrome('C:\chromedriver.exe',options=options)
browser.implicitly_wait(15) # 묵시적 대기, 활성화를 최대 15초가지 기다린다.

# 1)페이지 가져오기(이동)
browser.get('https://www.naver.com')


# 2)페이지 이동
time.sleep(2)
browser.find_element_by_css_selector('a.nav.shop').click()

# 3)쇼핑검색창 클릭
search = browser.find_element_by_css_selector('.co_srh_input')
search.click()

# 4)검색어 입력
search.send_keys("아이폰 13")
search.send_keys(Keys.ENTER)

# 5초후 종료
time.sleep(36000)
browser.quit() # 웹 브라우저 종료. browser.close()는 탭 종료