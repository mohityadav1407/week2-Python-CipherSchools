x = 6
x = 'anuj'
x = 1.5
print(x)

def show_loading():
    for _ in range(3):
        print("loading...")
         

a = 5
a = 7

print(a + b)
show_loading()

print(a - b)
show_loading()

print(a*b)
show_loading()



# function can take parameters

def sheldon_knock(name):
    for _ in range(3):
        print("knock knock knock",name)

sheldon_knock("leonard")


def sheldon_knock(name,time=3):
    for _ in range(time):
        print("knock knock knock",name)


def add(a+b):
    return a+b

a=add(1,2)
print(a)