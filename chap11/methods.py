#super() methods
'''class Person:
    country = "india"
    def workout(self):
        print("exercise daily")

class Employee(Person):
    company = "goole"
    def getSalay(self):
        super().workout()
        print("SALARY IS 99999")

class Programmer(Employee):
    company = "fiver"
    def getSalay(self):
        super().getSalay()
        print("SALARY will be added to employee")

p = Person()
e = Employee()
pr = Programmer()
#e.workout()
#pr.workout()
pr.getSalay()
'''

#using as constructor
'''class Person:
    
    country = "india"
    def __init__(self):
        print("person is made")
    def workout(self):
        print("exercise daily")

class Employee(Person):
    company = "goole"
    def getSalay(self):
        super().__init__()
        print("SALARY IS 99999")

class Programmer(Employee):
    company = "fiver"
    def getSalay(self):
        super().__init__()
        #super().getSalay()
        print("SALARY will be added to employee")

p = Person()
e = Employee()
pr = Programmer()
#e.workout()
#pr.workout()
pr.getSalay() '''


