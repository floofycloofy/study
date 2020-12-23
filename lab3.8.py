from random import randint 
while True:
	A = []
	B = []
	M,N = input('Введит M и N через пробел: ').split()
	for i in range(int(N)):
		A.append ([])
		for j in range(int(M)):
			A[i].append(randint(10,99))
	for i in range(int(N)):
		B.append ([])
		for j in range(int(M)):
			B[i].append(A[int(M)-i-1][int(N)-j-1])
		B[i][int(M)-i-1] = A[i][int(M)-i-1]
	for i in range(int(N)):
		print(A[i])
	print('\n')	
	for i in range(int(N)):
		print(B[i])