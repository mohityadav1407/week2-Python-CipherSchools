{1,2,3,4,5}
a = {1,2,3,4}
type(a)
a = {"name":"anuj"}
type(a)

for i in a:
    print(i)

a.add(7)
a.remove(3)
a.add(2)

for i in a:
    print(i)

a = {1,2,3,4}
b = {1,2,3,4}
a - b

a.union(b)

a.inersection(b)

a.add(1)

a.remove()

a

a = [[''] * 3
] * 3
a[1][1] = 'X'
a

print(id(a[0][1]))
print(id(a[2][1]))
print(id(a[1][1]))

a =[1,2,3,4,5]

a[0] = 100
a = 1
id(a)

a = 2
id(a)


class Student:
    name = "Tony"
    marks = 60

a = 258
b = 258

print(a == b)
print(a is b)



a = "anuj"
hash(a)