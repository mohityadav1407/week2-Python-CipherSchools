""" Abstraction
    Encapsulation
    Polymorphism
    Inheritance """

student1 = {
    "name" : "Anuj Verma"
    "marks" : 100
}

student2 ={
    "name" : "Samarth"
    "marks" : 82
}

# coupling and Cohesion

# abstraction : need to know basis

class Person:
    pass
p = Person() 
print p

id(p)

def square(a):
    print(a**2)

a = 1
a.square

class Person():
    name = "anuj"
    def say_hi(self):
        print(f"Hello Everyone : I am {self.name}")
        
p = person()
p.say_hi