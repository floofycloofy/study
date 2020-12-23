import time
from tkinter import * 
root = Tk()
canvas = Canvas(root, width = 500, height = 500) 
canvas.pack()
while True:  
	a,b = input('Введите координаты центра круга(поле 500х500)(2 числа через пробел): ').split(' ')
	a = int(a)
	b = int(b)
	krug = canvas.create_oval(a-50,b-50,a+50,b+50)
	root.update()
	time.sleep(5)
root.mainloop   