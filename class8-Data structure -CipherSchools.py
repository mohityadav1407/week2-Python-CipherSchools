""" Comprehension """

a = []
for i in range(5):
    a.append(i)
print(a)

[ i for i in range(5) ]

a = []
for i in range(5):
    temp = []
    for j in range(5):
        temp . append(j)
    a.append(temp)

print(a)

n = 5

[  [ max(i+1,j+1,n-1,n-j) for j in range(n)] for i in range(n)]

a = []
for i in range(2):
    for j in range(2):
        a.append(j)


[ [] for i in range(2) for j in range()]


{
    2:4
    3:9

}

{ i:i**2 for i in range(5)}
{ i for i in range(5) }

a = (i for i in range(5))

it = iter(a)

next(it)

