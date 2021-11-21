import pyautogui
import pyperclip

# 1. 키보드 입력
def write():
  for i in range(5):
    pyautogui.write('ggit')


# write()
# 2. 키 입력
def keypress():
  pyautogui.press('enter')
  pyautogui.press('up')

# 3. 동시키 입력
def dongsikeypress():
  pyautogui.hotkey('ctrl','c')

# 4. 한글입력
def hangul_write():
  pyperclip.copy('print("정신나갈거같아")')
  for i in range(3):
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
