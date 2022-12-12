1 + 2

'anuj' * 2

lambda a,b:a +b

print("Hello World")

show = print

show("something")

def func():
    return 1 + 4

a = func

name = ["anuj","santosh","wednesday","jenna"]

for name in names:
    print(name)

#itertools

for name in enumerate(names):
    print(name[0],name[1])


int a{} = {1,2,3}

# methods of swapping values
a = 5
b = 9

temp = a
a = b
b = temp

a = 5
b = 9

a = a^b
b =a^b
a = a^b
print(a ,b)
# packing and unacking values
a = 5
b = 9

a,b = b,a
print(a,b)


a = [1,2,3]
b,c,d = a

a = 1,2


for i,name in enumerate(names):
    print(i,"-",name)


name = ["anuj","santosh","wednesday","jenna"]
scores = [100,12,52,100]
states=["punjab","delhi","bihar","punjab"]

for name,score,state in zip(names,scores,states):
    print(name,"-",score)