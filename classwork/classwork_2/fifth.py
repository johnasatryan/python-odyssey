m = 0
n = 0


import random

m = int(input("Enter m: "))
n = int(input("Enter n: "))


matrix = [[random.randint(10, 99) for _ in range(n)] for _ in range(m)] 

max_number = matrix[0][0]

print(matrix)

for i in range(m):
	for j in range(1, n):
		if max_number < matrix[i][j]:
			max_number = matrix[i][j]


print(max_number)
