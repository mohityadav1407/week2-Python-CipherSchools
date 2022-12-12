a = [1,2,3]

a[0] = 100
a[2] = 200
a

a = (1,2,3,4)

type(a)

def func(*args):
    print(type(args))

a = 5
b = 9
a,b = b, a

c =a,b

def sum_diff(a,b):
    s = a+b
    d= a-b

    return s,data

c = sum_diff(5,6)


a = (1,2,3,4)
list(range(5))

tuple(range(5))

a = (1,2,3,4,5,6)
a.append(9)
a.append(8)

# Dictionary
a = dict{}
a["name"]

a = {
    "name":"Anuj Verma",
    1:"dsdasds"
    (1,2):"Sds"

}

a[1]
a["name"]
a[(1,2)]

a["name"] = "akaf"
a = {
    "name":"John"
    "Company":"shuttl"
    "college":"IPU"
}

a["marks"]

key = "marks"
if key in a:
    print(a[key])
else:
    print("key doesn't exist")



key = "marks"
print(a.get(key))

key = "marks"
print(a.get(key,"key doesn't exist"))

a.keys()

a.values()

for x in a.items():
    print(x)

print(key,"->",values)

for  x in a:
    print(a)

"name" in a

list(a)

