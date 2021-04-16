#function

#simple functio syntax
'''def dummyfun():
    print("i am dummy function")

dummyfun()

'''
'''marks1 =[45,65,67,87]
percentage1 = ((marks1[0] +marks1[1]+marks1[2]+marks1[3])/ 400) * 100
marks2 =[85,65,69,97]
percentage2 =(sum(marks2)/400)*100
print(percentage1, percentage2) '''


#grouping with fun
'''def percentage(marks):
    return ((marks[0] + marks[1] + marks[2] + marks[3]) / 400) * 100 #return = go with value
    
marks1 = [34, 45, 56, 67]
per1 = percentage(marks1)

marks2 = [56, 56, 78, 99]
per2 = percentage(marks2)

print(per1, per2)'''


#quick quiz
#wap to greet a user with "good day" using function
'''def greet(name):
    print("good day " + name) #function defination

name = input("enter your name")
greet(name) # function call

'''
#fun with argument
'''def add(num1, num2):
    return num1 + num2

s = add(2, 3)
print(s)
'''

#default parameter value
def greet(name="stranger"):
    print("good day " + name) #function defination

#name = input("enter your name")
greet() # function call