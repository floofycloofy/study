while True:
	N = int(input('Введите N: '))
	if N in range(-10,-4) :
		N *= 2
	elif N in range(-4,0) :
		N = abs(N)
	elif N in range(0,16) :
		N = 1
	else :
		N = 0
	print (N)