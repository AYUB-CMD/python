#Procedural oriented progamming
#normal way

'''a =12
b = 34
print("the sum of tow number :", a + b)
'''

#object oriented progamming

'''class Number:
    def sum(self):
        return self.a + self.b

num =Number()
num.a = int(input('enter your 1st number'))
num.b = int(input('enter your 2nd number'))
s = num.sum()
print(s) '''

#2nd example

class Railway:
    formType = 'Railway Form'
    def printData(self):
        print(f"Form Name {self.name} ")
        print(f"Train Name {self.train} ")

ayubRailwayInfo = Railway()
ayubRailwayInfo.name ="Ayub Thapa"
ayubRailwayInfo.train = "Rajdhani Express"
ayubRailwayInfo.printData() 