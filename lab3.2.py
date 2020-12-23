from random import randint 
while True:
	max = -100
	A = []
	N = input('Введит длину массива:')
	for i in range(int(N)):
		A.append (randint(-100,100))
	print (A)
	for i in range(int(N)):
		if A[i] >= max:
			max = A[i]
	print('Max = ', max)
	for i in range(int(N)):
		A[i]+= max
	print(A)