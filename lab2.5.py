sumx = 0
for i in range(10000):
	sum = 0
	for n in range(i - 1, 1, -1):
		if i % n == 0:
			sum+= i
	if sumx < sum:
		sumx = sum
		counter = i
print(counter)