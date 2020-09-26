while True:
	a,b,c = input('Введите 3 числа через пробел: ').split()
	if a > b and a > c :
		print('Число', a, 'максимальное', sep = ' ')
	elif b > c :
		print('Число', b, 'максимальное', sep = ' ')
	else:
		print('Число', c, 'максимальное', sep = ' ')