# modes (r, w, a)


#fs = open('file4.txt', mode='rb')

#text = fs.read()

#print(text)
#print(fs.tell())
#text2 = fs.read()

#print(text2)


# seek and teel

#fs.seek(2)

#print(fs.read())

fs = open('file5.txt', 'r')

#fs.write("Hello Python")

#fs.seek(0)
print(fs.fileno())
