class Emp:
    compamy = "resort"
    salary = 9999
    salaryBonus = 989
    #totalSalary= 9999+989

    @property #if u dont want to print u just want ot get value then use property decorator
    def totalSalary(self):
        return self.salary + self.salaryBonus
        
e = Emp()
print(e.totalSalary)  #it is function but act as property with property decorator
#it is called getter method also   