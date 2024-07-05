# 1. 

ls = [3, 1, 2, 3, -4, 2]

min = ls[0]
min_index = 0
max = ls[0]

for i in range(1, len(ls)):

	if min > ls[i] and min > 0:
		#print("hello")
		min = ls[i]
		max = ls[i]

	
#print(f"minimum is: {min}")
#print(f"maximum is: {max}")

# 4. 
sum = 0
mul = 1

for i in ls:
	sum = sum + i
	mul = mul * i

#print(sum)
#print(mul)


nor_list = [43, 12, 54, 11]

size = len(nor_list)

for i in range(size):
	nor_list[i] = nor_list[i] / size
	
for i in ls:
	i = "hello"

print(nor_list)


# 8

size = int(input("Please enter size of our new list: "))



ls = []

for i in range(size):
	digit = input(f"Please enter a valid digit for {i} position: ")
	new_str = ""
	for char in digit:
		if ord(char) >= 48 and ord(char) <= 57 or char == ".":
			new_str += char
	
	print(float(new_str))
		

print(ls)
	





