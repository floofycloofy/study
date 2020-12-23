from random import randint 
while True:
	max = -100
	A = []
	M,N = input('Введит M и N через пробел: ').split()
	for i in range(int(N)):
		A.append ([])
		for j in range(int(M)):
			A[i].append(randint(-100,100))
	for i in range(int(N)):
		print(A[i])
	for i in range(int(N)):
		for j in range(int(M)):
				if A[i][j] >= max:
					max = A[i][j]
		print(A[i], 'Максимальное: ', max)
		max = - 100
