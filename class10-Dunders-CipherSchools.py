""" Dunders """
"""  __<name of dunders>__ """
 


class Person:
    def __init__(self,name):
        self.name  = name
    def say_hi(self)
    print('Hello, my name is',self.name)

p = Person('Anuj')
p.say_hi()

a = 1
a + 1
str(a)

for i in a:
    print(i)

class A:
    def __init__(self):
        print(self)
        print("initialized")
    
    def __del__(self):
        print(self)
        print("I am dying")

del a

a = 1
type(a)

a+5

a.__add__(5)

"anuj" * 2

"anuj".__mul__(2)



class A:
    a = 1
    b = 2

    def __add__(self,x):
        return self.a + self.b + x