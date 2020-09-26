from math import sin 
while True:
	N = int(input('Введите N: '))
	a = 0
	for i in map(lambda x: x/10,range(0,N*10+1)): #сделать на форе звучало как вызов
		a += sin(i)
		print (a)
	print (a)