while True:
	x,y = map(int, input('Введите x и y через пробел: ').split())
	if x > y :
		xn = 2*(x*y)
		yn = (x+y)/2
	else:
		yn = 2*(x*y)
		xn = (x+y)/2
	print('X =',xn,'Y =',yn)