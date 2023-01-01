import numpy

n = int(input())
A = []
for i in range(n):
    l = list(map(float, input().split()))
    A.append(l)
    
print(round(numpy.linalg.det(A), 2))