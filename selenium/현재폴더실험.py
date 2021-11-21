import os
import time
import csv
cf = os.getcwd()
ee = "ee.jpg"

print(fr"{cf}\{ee}")

mkd = os.mkdir("eef")
time.sleep(2)
# os.chdir(r'C:\Users\jaws\Desktop\crwal\eef')
f = open(r'C:\Users\jaws\Desktop\crwal\eef','w',encoding='utf-8', newline='')
writer = csv.writer(f)