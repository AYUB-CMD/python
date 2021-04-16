#file i/o

#use open fun to read content of a file
#by default the mode is r which is read
f = open('chap9/sample.txt', 'r')
#data = f.read()
#data = f.read(3) print first 3 character of that content

#print(data)
f.close()

a = f.readline() #reads one line from the file
print(a)
