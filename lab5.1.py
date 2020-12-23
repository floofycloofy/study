import math 
import time 
from tkinter import * 
root = Tk()
canvas = Canvas(root, width = 500, height = 500) 
canvas.pack()
while True:  
  time_now = time.localtime()
  time_sec = int(time.strftime("%S", time_now))  
  sec_angle = 6 * time_sec
  line_sec = canvas.create_line(250,250, 250 - 180 * math.cos(sec_angle * math.pi/180 + math.pi/2),250 - 180 * math.sin(sec_angle * math.pi/180 + math.pi/2),width =2, fill = 'red') 
  root.update()
  canvas.delete(line_sec) 
root.mainloop   