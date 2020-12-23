while True:
	M,N = input('Введите 2 числа через пробел: ').split()
	if M >= N:
		a = int(M)
		b = int(N)
	else:
		a = int(N)
		b = int(M)
	while b > 0:
		r = a % b
		a = b
		b = r
	print (' Наибольший общий делитель:',a,'\n','Наименьшее общее кратное:',abs(int(M)*int(N))/a)
