#https://www.youtube.com/watch?v=1b7pXC1-IbE
# from urllib.request import Request, urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request


#밑에 두줄은 환경세팅
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36")

#브라우저생성
browser = webdriver.Chrome('C:\chromedriver.exe',options=options)
browser.get("http://www.google.com")

#클릭
searchbar = browser.find_element_by_name('q')
searchbar.click()
time.sleep(1)
searchbar.send_keys("조코딩")
searchbar.send_keys(Keys.ENTER)

#이미지탭 클릭함
browser.find_element_by_css_selector('.hdtb-mitem a').click()
images_thumnails = browser.find_elements_by_css_selector('.rg_i.Q4LuWd') #여러개 이미지 썸네일

count =1
for image in images_thumnails:
  image.click()
  time.sleep(3)
  imgurl = browser.find_element_by_css_selector('.n3VNCb').get_attribute("src")

#403에러방지 아래로3줄 씨발 이것땜에 눈물이ㅠㅠ
  opener=urllib.request.build_opener()
  opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36')]
  urllib.request.install_opener(opener)

#이미지 다운로드
  #폴더경로는 알아서 처리하셈
  urllib.request.urlretrieve(imgurl, fr"C:\Users\jaws\Desktop\crwal\project\selenium\{count}.jpg")
  count +=1












time.sleep(36600)
browser.quit()




# assert "Python" in browser.title
# searchbar.clear()
# searchbar.send_keys("pycon")
# searchbar.send_keys(Keys.RETURN)
# assert "No results found." not in browser.page_source
# browser.close()

