while True:
	a,n = input('Введите a и n через пробел: ').split()
	a = float(a)
	n = int(n)
	b = a
	for i in range(1,n):
		b *= a+i
	print(b)