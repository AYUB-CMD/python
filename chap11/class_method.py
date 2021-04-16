class Emp:
    company = "amazon"
    salary = 999
    localation = "usa"

    '''def change(self, sal):
        self.__class__.salary = sal '''
    @classmethod    #decorator
    def change(cls, sal):
        cls.salary = sal    

e = Emp()
print(e.salary)
e.change(9955)
print(e.salary)