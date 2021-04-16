#self
'''class Emp:
    company="Google"
    def getSalary(self):
        print(f"Salary for Employee woring in this company {self.company}  is {self.salary} ")
       

ayub = Emp()
ayub.salary = 10000
 #equivalent to Emp.getSalary(ayub) with self parameter
ayub.getSalary() 
'''
#static method
'''class Employee:
    company= "Amazon"

    def get(self,signature):
        print(f" {self.salary} \n{signature} ")
    @staticmethod #without self parameter
    def greet():
        print("hello")

ayub=Employee()
ayub.salary = 9999
ayub.get("thanks")
ayub.greet()
'''
#constructor
#__int__()
'''class Emp1:
    company: "google"
    def __init__(self):
        print("Employee is created")


ayub =Emp1()
'''

'''class Emp1:
    company = "google"
    def __init__(self, name, salary, company):
        self.name = name
        self.salary = salary
        self.company=company
        print("Employee is created")
    def info(self):
        print(f" name : {self.name}")
        print(f" salary : {self.salary}")
        print(f" company : {self.company}")

ayub = Emp1("ayub", 1000, "google")
#ayub = Emp1() throws an error
ayub.info()'''