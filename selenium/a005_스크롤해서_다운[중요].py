#https://www.youtube.com/watch?v=1b7pXC1-IbE
# from urllib.request import Request, urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os


#밑에 두줄은 환경세팅[필수]
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36")

#브라우저생성[필수]
browser = webdriver.Chrome('C:\chromedriver.exe',options=options)
browser.get("http://www.google.com")

#클릭
search_item = input('다운받고 싶은 이미지 쓰세요>>>>')
searchbar = browser.find_element_by_name('q')
searchbar.click()
time.sleep(1)
searchbar.send_keys(f"{search_item}")
searchbar.send_keys(Keys.ENTER)
time.sleep(1)

#이미지탭 클릭함
browser.find_element_by_css_selector('.hdtb-mitem a').click()



# 무한베기
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
      try:
        browser.find_element_by_css_selector('.mye4qd').click()
      except:
        break
    last_height = new_height

#여러개 이미지 썸네일
images_thumnails = browser.find_elements_by_css_selector('.rg_i.Q4LuWd')

count =1
os.mkdir(f"{search_item}")
for image in images_thumnails:
  try:
    image.click()
    time.sleep(2)
    imgurl = browser.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute("src")

    #403에러방지 아래로3줄[필수]=============개 중 요===============================
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36')]
    urllib.request.install_opener(opener)

    current_dir = os.getcwd()#현재폴더 값
    current_dir = f"{current_dir}\{search_item}"

    #이미지 다운로드 폴더경로는 알아서 처리하셈
    urllib.request.urlretrieve(imgurl, f"{current_dir}\{search_item}-{count}.jpg")
    count +=1
  except:
    pass



time.sleep(36600)
browser.quit()
