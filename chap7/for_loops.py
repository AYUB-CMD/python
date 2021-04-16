#for loop
'''fruits = ["banana", "apple", "grapes", "mangoes"]

for item in fruits:
    print(item) '''

#range

'''for i in range(1,8,2):#if u want to start from 1 to 7 then for i in range(1,8):
    print(i)
    '''
#step-size for i in range(1,8,2): (start,stop,step-size) which means skip (2)and print
 


#for else loop

'''for i in range(10):
    print(i)
else:
    print("done") '''
    


#break statement
'''for i in range(100):
    print(i)
    if (i == 3):
        break '''
        
#continue statement it skipped the number
for i in range(10):
    if i == 5:
        continue
    print(i)

#pass statement
i = 4

if i < 0:
    pass