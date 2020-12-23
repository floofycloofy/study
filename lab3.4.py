from random import randint 
while True:
	sum= 0
	p = 1
	A = []
	N = input('Введит длину массива:')
	for i in range(int(N)):
		A.append (randint(-100,100))
	print (A)
	for i in range(int(N)):
		sum+= A[i]
		p*= A[i]
	print('Cумма: ', sum, '\n', 'Произведение: ', p,'\n', 'Среднее арифмитическое: ', sum/int(N))