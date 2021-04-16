#inheritance

#single inheritance
'''class Employee:
    company = "Goole"
    def showDetails(self):
        print("This is Employee")

class Programmer(Employee):
    language = "Python"
    def getLang(self):
        print(f"Language is {self.language}")
    def showDetails(self):
        print("This is Programmer ") #overwriting
e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)'''

#multiple inheritance
'''class Employee:
    company = "Goole"
    ecode =122
class Freelancer:
    company = "Fiver"
    level = 0
    def upgradeLevel(self):
        self.level = self.level+1

class Programmer(Employee, Freelancer):
    name = "ayub"
    

p = Programmer()
p.upgradeLevel()
print(p.level)
#print(p.company) #fifo in programmer class'''


#multilevel inheritance
#if they have methods then they will otherwise they will inherit from nearest class
'''
class Person:
    country = "india"
    def workout(self):
        print("exercise daily")

class Employee(Person):
    company = "goole"
    def getSalay(self):
        print("SALARY IS 99999")

class Programmer(Employee):
    company = "fiver"
    def getSalay(self):
        print("SALARY will be added to employee")

p = Person()
e = Employee()
pr = Programmer()
e.workout()
pr.workout() '''     


       