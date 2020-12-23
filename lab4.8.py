while True:
	a = input('Введите строку: ')
	l = len(a)
	A = []
	B = []
	for i in range(l):
		if (ord(a[i])>47) and (ord(a[i])<58):
			A.append(a[i])
		else:
			B.append(a[i])
	a = ''
	a = ''.join(A + B)
	print(a)