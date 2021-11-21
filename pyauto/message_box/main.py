import pyautogui as pg

#alert
def jasin():
  pg.alert('자신있나')
  pg.moveTo(500,500)
  pg.moveTo(1000,500)
  pg.moveTo(500,500)
  pg.moveTo(1000,500)
  pg.moveTo(500,500)
  pg.alert('끝')

#yes no 박스
def message_confirm_box():
  a = pg.confirm(text='내용임',title='제목임')#메시지가 들어가는거임 디폴트는 yes, cancel
  print(a)

#인풋박스
def inputbox():
  b = pg.prompt(text='내용ㅇ',title='제목',default='입력해라')#b안에는 디폴트로 입력해라가 들어감
  print(b)

#패스워드 
def pw():
  a = pg.password(text='내용입니다', title='제목입니다', default='입력하세요', mask='*')
  print(a)
