while True:
	a = input('Введите строку: ')
	l = len(a)
	A = []
	for i in range(l):
		A.append(a[l-i-1])
	a = ''
	a = ''.join(A)
	print(a)