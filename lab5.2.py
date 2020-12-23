from tkinter import * 
root = Tk()
canvas = Canvas(root, width = 500, height = 500) 
canvas.pack()
while True:  
	for i in range(0,25):
		line1 = canvas.create_line(25*i,0,25*i,500)
		line2 = canvas.create_line(0,25*i,500,25*i)
		root.update()
root.mainloop   