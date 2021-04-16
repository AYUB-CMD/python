#1
'''class Programmer:
    comapny = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product=product
    def info(self):
        print(f"Worker Name: {self.name} Comapany:{self.comapny} and his and her product : {self.product} ")
ayub = Programmer("ayub", "github")
ayub.info()
anuj = Programmer("anuj", "skype")
anuj.info() '''

#2
'''class Calculator:
    def __init__(self, num):
        self.number = num
    def square(self):
        print(f"The square of number {self.number} is {self.number **2} ")
    def cube(self):
        print(f"The cube of number {self.number} is {self.number **3} ")
    def squareRoot(self):
        print(f"The squareRoot of number {self.number} is {self.number **0.5} ")

a = Calculator(2)
a.square()
a.cube()
a.squareRoot()
      '''

#3
'''class Sample:
    a = "ayub"
    
obj = Sample()
obj.a = "ninja"

print(Sample.a)
#if u want to chaneg class atrributes than use Sample.a ="ninja"
print(obj.a)
'''
#4   

'''class Calculator:
    def __init__(self, num):
        self.number = num
    def square(self):
        print(f"The square of number {self.number} is {self.number **2} ")
    def cube(self):
        print(f"The cube of number {self.number} is {self.number **3} ")
    def squareRoot(self):
        print(f"The squareRoot of number {self.number} is {self.number **0.5} ")
    @staticmethod
    def greet():
        print(f"hello user ")


a = Calculator(2)
a.square()
a.cube()
a.squareRoot()
a.greet() '''

#5
'''class Train:
    def __init__(self, name, fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        
    def getStatus(self):
        print(F"The Name of the train is {self.name}")
        print(F"The fare of this train : {self.fare}")
        print(F"Seats available {self.seats}")
    def fareInfo(self):
        print(F"The fare of this train : {self.fare}")

    def bookTickect(self):
        if (self.seats>0):
            print(f"your ticket has been booked and your seat number is {self.seats}")
            self.seats = self.seats-1   
        else:
            print("full")

    def cancleTicket(self, seatsNo):
        pass
        


intercity = Train("Intercity express : 142", 90, 2)

intercity.fareInfo()
intercity.bookTickect()
intercity.bookTickect()
intercity.bookTickect()
intercity.getStatus()'''

#6
'''class Sample1:
    def prob6(seli):
        print(seli.name)

a = Sample1()
a.name = "ayubh"

print(a.name)'''
