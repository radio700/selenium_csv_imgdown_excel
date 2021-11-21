import time


for i in range(10):

  total_time = time.ctime()
  year = total_time.split(' ')[4]
  month = total_time.split(' ')[1]
  day = total_time.split(' ')[2]
  ctime = total_time.split(' ')[3]

  print(year, month, day, ctime)
  time.sleep(1)

