#1
'''f = open('chap9/poems.txt')
t = f.read()
if 'twinkle' in t:
    print("its present")
else:
    print("not present")
f.close() '''

#2 ✔

#3✔
#4
'''with open('chap9/sample.txt') as f:
    content = f.read()
content = content.replace("donkey", "##@@$$$52@")
with open('chap9/sample.txt','w') as f:
   f.write(content) '''
   
#5
'''words =['fuck','lick','suck']
with open('chap9/sample.txt') as f:
    content = f.read()
for word in words :   
    content = content.replace(word, "##@@$$$52@")
with open('chap9/sample.txt','w') as f:
   f.write(content) '''
   

#6
'''with open("chap9/log.txt") as f:
    c = f.read().lower()
if 'python' in c:
    print("python is present")
else:
    print("nope") '''  
    
#7
'''content = True
i=1
with open('chap9/log.txt') as f:
    while content:
        content = f.readline()
        
        if "python" in content.lower():
            print(content)
            print(f"yes it is present on line no: {i}")
            print(i)
            i += 1
          '''
    
#8
'''with open('chap9/this.txt') as f:
    c = f.read()
with open('chap9/copy.txt','w') as f:
    f.write(c) ''' 
    

#9
'''file1 = 'chap9/copy.txt'
file2 = 'chap9/this.txt'

with open(file1) as f:
    f1 = f.read()
    
with open(file2) as f:
    f2 = f.read()

if f1 == f2:
    print("file are same")
else:
    print("no") '''  
    


#10
'''file1 = 'chap9/copy.txt'
with open(file1,'w') as f:
    f.write("")'''

#11    
#rename

import os

oldname = 'chap9/sample2.txt'
newname = "chap9/renamed_by_python.txt"

with open(oldname) as f:
    c = f.read()


with open(newname,'w') as f:
    f.write(c)

os.remove(oldname)
