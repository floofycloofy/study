while True:
	a = input('Введите строку: ')
	l = len(a)
	for i in range(l):
		if a[i] == ' ':
			ind = i
	a = a[0:ind]
	print(a)