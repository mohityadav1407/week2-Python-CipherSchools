def func(a,b,c):
    print(a)
    print(b)
    print(c)

func(c=1,a=2,b=3)

def funca(a):
    print(a)

def hello():
    print("Hello World")
    return 1

a = 1
a = hello

a()

hello = 2
print(hello)

print(1,2,3,4,5,sep=",")


def function(a,b = 10,c):
    print(a,b,c)

func(1,c=5)

#  *args  **kwargs


def funct(a,b):
    print(a,b)
func(1,2)

def func(a=1,b=2):
    print(a,b)
func()
func(1)
func(1,2)


def func(a,b,*c):
    print(a)
    print(b)
    print(C)
func(1,2,3,4)

def func(a,b,*c,d,e='anuj'):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

func(1,2,3,4,5,6,7,8,d=9,e='dsdfj')

def func(**k):
    print(k)

func(name='anuj')


def func(a , b = 1 , *c ,d ,e = '',**k):
    print(k)




x=lambda a , b :  a + b
ax(1,2)

a = None

func(a = lambda:print("hello"))

