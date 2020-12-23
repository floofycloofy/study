from random import randint 
while True:
	min = 100
	A = []
	N = input('Введит длину массива:')
	for i in range(int(N)):
		A.append (randint(-100,100))
	print (A)
	for i in range(int(N)):
		if A[i] <= min:
			ind = i
			min = A[i]
	print(min, ind)