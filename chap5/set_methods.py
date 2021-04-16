#set methods
b = set()  #empty 
print(type(b))
b.add(5)
b.add(2)
b.add(6)
b.add(9)
b.add(2)#adding a value repeatedly doesnot changes a set
print(b)

#u can add tuple not list
#because list is mutable tuple is not
#b.add([1, 2, 3, 4])❌
#b.add((1, 2, 3, 4) ) #✔
print(len(b))  #prints the length of b
print(b)

b.remove(5) #remove 5 from the set
print(b)

#pop
print(b.pop)
print(b)

#empty
#b.clear()

#union


#intersection