import numpy

n, m = map(int, list(input().split()))
l = []
for i in range(n):
    x = list(map(int, list(input().split())))
    l.append(x)
    
arr = numpy.array(l)
print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(round(numpy.std(arr, axis=None), 11))
