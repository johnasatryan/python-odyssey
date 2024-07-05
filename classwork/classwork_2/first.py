ls1 = [1, 2, 3, 4]
ls2 = [2, 2, 3, 4]


ls1_size = 0

for i in ls1:
	ls1_size += 1

ls2_size = 0

for i in ls2:
	ls2_size += 1



if ls1_size != ls2_size:
	print("sizes are not equal!")
else:
	flag = True
	for i in range(len(ls1)):
		if ls1[i] != ls2[i]:
			flag = False

if not flag: 
	print("Lists elements are not equal!")
else: 
	print("List elements are equal!")
