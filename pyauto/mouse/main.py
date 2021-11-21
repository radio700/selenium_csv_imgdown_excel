import pyautogui
import time

#화면크기
def size():
  print(pyautogui.size())

#마우스위치 출력
def mousewitch():
  time.sleep(2)
  print(pyautogui.position())

#마우스 위치 이동
def mouse_move():
  pyautogui.moveTo(41,442)
  pyautogui.moveTo(20,211,2)

#마우스 클릭
def clicking():
  pyautogui.click()
  pyautogui.rightClick()
  pyautogui.doubleClick()
  pyautogui.click(clicks=3,interval=1)


#마우스 드래그
#pyautogui.mouseInfo() 실행후에 A-B값 입력

def drag():
  pyautogui.moveTo(473,44,.2)
  pyautogui.dragTo(360,39,.2)

#마우스 스크롤
def scr():
  pyautogui.scroll(2,473,44)