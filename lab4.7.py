while True:
	answer = 'Nope!'
	a = input('Введите строку: ')
	l = len(a)
	for i in range(l-1):
		if a[i] == a[i+1]:
			answer = 'Yep!'
	print(answer)