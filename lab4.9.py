while True:
	a = input('Введите строку: ')
	l = len(a)
	A = []
	B = []
	for i in range(l):
		if a[i] == ' ':
			A.append(a[i])
		else:
			B.append(a[i])
	a = ''
	a = ''.join(A + B)
	print(a)