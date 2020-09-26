while True:
	N = str(input('Введите N: '))
	a = 1
	for i in range(len(N)):
		a *= int(N[i])
	print (a)