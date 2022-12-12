# string formatting or String Interpolation

a = 5
print("valie of a is %d" % (a))
print("Hello world")
print("value of a is {}".format(a))


a,b,c,d = 1,2,3,4
"a={2}, b={1} ,c={0}".format(c,b,a)

name = 'Anuj Verma'
comapny = 'Tech'
"Hello I am name = {name} and I work at company = {company}".format(name = name,company = company)

print(f"name = {10/3}")

len(r"a\nb")

for c in r"a\nb":
    print(c)

"   anuj ".strip()

"1,2,3,4,5".split(" ,")

"anuj verma".replace("a","z")

"anuj verma".count("a")