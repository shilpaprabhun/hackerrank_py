import numpy

n = int(input())
A = []
for i in range(n):
    x = list(map(int, list(input().split())))
    A.append(x)
    
b = []
for i in range(n):
    x = list(map(int, list(input().split())))
    b.append(x)

B = []
for j in range(n):
    l =[]
    for i in range(n):
        l.append(b[i][j])
    B.append(l)

result = []
for i in range(n):
    l =[]
    for j in range(n):
       # print(numpy.array(A[i]), numpy.array(B[j]))
        l.append(numpy.dot(numpy.array(A[i]), numpy.array(B[j])))
    result.append(l)

print(numpy.array(result))