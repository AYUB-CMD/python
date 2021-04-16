#Class Attribute

'''class Employee:
    company = "Google" #specific to each class
    
ayub = Employee() #instantiating object
anuj = Employee()
print(ayub.company)
print(anuj.company)
Employee.company = "youtube"
print(ayub.company)
print(anuj.company)
'''

#Instance Attribute

class Employee:
    company = "Google" #specific to each class
    salary =10000
ayub = Employee() #instantiating object
anuj = Employee()

Employee.company = "youtube" #changing class attributes
ayub.salary = 99000 #changing and adding class attributes
anuj.salary = 89000

print(ayub.salary)
print(anuj.salary)