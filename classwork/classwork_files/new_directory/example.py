

fs = open('example2.py', 'w')


code = '''

x= 14

y = 25

print(x + y)

'''

fs.write(code)

# Context manager

fs.close()

