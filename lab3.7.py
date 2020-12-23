from random import randint 
while True:
	max = -100
	A = []
	B = []
	M,N = input('Введит M и N через пробел: ').split()
	for i in range(int(N)):
		A.append ([])
		for j in range(int(M)):
			A[i].append(randint(-100,100))
	for i in range(int(N)):
		print(A[i])
	for i in range(int(N)):
		for j in range(int(M)):
				B.append(A[i][j])
	print(B)