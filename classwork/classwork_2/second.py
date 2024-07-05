ls = []

length = 5

for i in range(length):
	tmp = input(f"Insert list {i}rd element: ")

	if not tmp.isdigit():
		print("Input is not valid number")
	else:
		ls.append(int(tmp))


if len(ls):
	min = ls[0]
	max = ls[0]

	min_index = 0
	max_index = 0
	
	for i in range(1, len(ls)):
		if ls[i] > max:
			max = ls[i] 
			max_index = i
		elif ls[i] < min:
			min = ls[i]
			min_index = i


print(max_index - min_index)



