'''class Number:
    def __init__(self,num):
        self.num = num
    def __add__(self,num2):
        print("lets add")
        return self.num+num2.num
    def __mul__(self,num2):
        print("lets mul")
        return self.num*num2.num  
n1 = Number(3)
n2 = Number(4)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul) '''

#other dunder methods (__init__)

class Number:
    def __init__(self,num):
        self.num = num
    def __add__(self,num2):
        print("lets add")
        return self.num+num2.num
    def __mul__(self,num2):
        print("lets mul")
        return self.num*num2.num  
    def __str__(self):
        return f"decimal numer : {self.num} "
    def __len__(self):
        return 1

n = Number(9)
print(n) #try this without __str__ and __len__ method u will know why
print(len(n))#try this without __str__ and __len__ method u will know why