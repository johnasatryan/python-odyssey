import numpy as np

matrix = np.zeros((3, 3))


#for i in range(len(matrix)):
	#for j in range(len(matrix[i])):
		# matrix[i][j] = int(input(f"Enter an integer in matrix [{i}][{j}] position: "))


[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

ls = [[None for _ in range(3)] for _ in range(3)]

for i in range(len(ls)):
	for j in range(len(ls[i])):
		ls[i][j] = int(input(f"Enter an integer in ls[{i}][{j}]: "))



for i in range(len(ls)):
	for j in range(len(ls[i])):
		print(ls[i][j], end=" ")
	print()


	
