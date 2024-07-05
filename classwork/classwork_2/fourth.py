ls = [[x + y for x in range(3)] for y in range(0, 9, 3)]

for i in ls:
	for j in i:
		print(j, end=" ")
	print(" ")


sum = 0
for i in range(len(ls)):
	sum += ls[i][i]


for i in range(len(ls)):
	print(ls[i][len(ls) - i - 1], end=" ")
