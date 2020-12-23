while True:
	M,N = input('Введите M И N через пробел: ').split()
	for i in range(int(N)):
		sum = 0
		n = i
		while n > 0 :
			sum+= n%10
			n = n//10
		if sum * sum == int(M):
			print(i)