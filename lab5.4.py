import time
from tkinter import * 
root = Tk()
canvas = Canvas(root, width = 500, height = 500) 
canvas.pack()
while True:  
	a,b,c = input('Введите координаты левого верхнего угла(поле 500х500) и длину стороны(3 числа через пробел): ').split(' ')
	a = int(a)
	b = int(b)
	c = int(c)
	krug = canvas.create_rectangle(a,b,a+c,b+c)
	root.update()
	time.sleep(5)
root.mainloop   