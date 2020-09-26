while True:
	a,b,c = input('Введите 3 числа через пробел: ').split() #Сортировка массива через 1 функцию слишком нагло поэтому вот вам переборчик
	if a > b and a > c :
		n1 = a
		if b > c:
			n2 = b
			n3 = c
		else:
			n2 = c
			n3 = b
	elif b > c :
		n1 = b	
		if a > c:
			n2 = a
			n3 = c
		else:
			n2 = c
			n3 = a
	else:
		n1 = c
		if a > b:
			n2 = a
			n3 = b
		else:
			n2 = b
			n3 = a
	print(n3,n2,n1)
