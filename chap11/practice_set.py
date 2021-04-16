#1 vector

'''class C2d:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j
    def __str__(self):
        return f" {self.icap}i+{self.jcap}j"

class C3d(C2d):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k
    def __str__(self):
        return f" {self.icap}i+ {self.jcap}j +{self.jcap}j"

v2d = C2d(1, 3)
v3d = C3d(1, 9, 7,)
print(v2d)
print(v3d) '''   

#2
'''class Animals:
    animlasTypes="mammal"
    
class Pets(Animals):
    colour="white"
    
class Dog(Pets): 
    @staticmethod
    def bark():
        print("woof woof")
        
d = Dog()
d.bark() '''   

#3
#salaryAfterIncrement =salar * increment

'''class Employee:
    salar = 1000
    increment = 1.5
    @property
    def salaryAfterIncrement(self):
        return self.salar * self.increment
        
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sai):
         self.increment = sai / self.salar
         
e = Employee()
print(e.salar)
print(e.salaryAfterIncrement) '''

#4
#formula
#(a+bi)(c+di)=(ac-bd)+(ad+bc)i
class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, c):
        return Complex(self.real + c.real, self.imaginary + c.imaginary)
    def __mul__(self, c):
        mulReal = self.real * c.real - self.imaginary * c.imaginary
        mulImg=self.real * c.imaginary + self.imaginary * c.real
        return Complex(mulReal,mulImg)    
    def __str__(self):
        if self.imaginary<0:
            return f" {self.real} - {-self.imaginary}i " 
        else:    
        return f" {self.real} + {self.imaginary}i "    
c1 = Complex(3, 2)
c2 = Complex(1, 7)
print(c1 + c2)
print(c1 * c2) 

#5

'''class Vector:
    def __init__(self, vec):
        self.vec = vec
    def __str__(self):
        str1 = ""
        index =0
        for i in self.vec:
            str1 += f"{i} a{index} +"
            index += 1
        return str1[:-1]
v1 = Vector([1, 4, 6,54,65,3])
print(v1)
'''
    