while True:
	a = input('Введите строку: ')
	l = len(a)
	for i in range(l):
		a[i] = chr(int(ord(a[i])+1))
	print(a)