#1
'''
n1 = int(input("enter your number"))
n2 = int(input("enter your number"))
n3 = int(input("enter your number"))
n4 =int(input("enter your number"))

if (n1 > n4):
    f1 = n1
else:
    f1 = n4

if (n2 > n3):
    f2 = n2
else:
    f2 = n3

if (f1 > f2):
    print(str(f1)+" is greatest")
else:
   print(str(f2)+ " is greatest") 
'''   

#2
'''
sub1 = int(input("enter your sub1 marks"))
sub2 = int(input("enter your sub2 marks"))
sub3 = int(input("enter your sub3 marks"))

if (sub1 < 33 or sub2 < 33 or sub3 < 33):
    print("your'e fail")

elif ((sub1 + sub2 + sub3) / 3 < 40):
     print("your'e fail")
else:
    print("passed")
   '''

#3

'''
comment = input("enter your text")

if ("make a lot of money" in comment):
    spam =True
elif ("go" in comment):
    spam = True
elif ("wow" in comment):
    spam = True
else:
    spam = False
    
if (spam):
    print("yes")
else:
    print("no")
    '''

#4
'''
text = input("enter your name")
if (len(text) < 4):
    print("less than 4 character")
else:
    print("good")   
    ''' 

#5

'''
lyst = ["ayub", "noinn", "ninja"]
name = input("enter your name")

if name in lyst:
    print("present")
else:
    print("not present")   
    '''

#6

'''
marks = int(input("enter your marks"))

if (marks >= 90 and marks <=100):
    print("ex")
elif (marks >= 80 and marks == 89):
    print("a")
elif (marks >= 70 and marks == 79):
    print("b")
elif (marks >= 60 and marks == 69):
    print("c")
elif (marks >= 50 and marks == 69):
    print("d")
else:
    print("fail")    
    '''

#7

post = input("enter your post")


if (post.find("Harry")or post.find("harry") in post):
    print("yes")
else:
    print("no")    