#URL - https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

def can_stack(d, l):
    while len(d) > 0:  
        x = l[-1] if len(l) > 0 else 2**31
        if len(d) == 1:
            if d[0] <= x:
                l.append(d.pop())
            else:
                l.clear()
                break
        else:
            if d[0] > d[-1] and d[0] <= x:
                l.append(d.popleft())
            elif d[0] < d[-1] and d[-1] <= x:
                l.append(d.pop())
            elif d[0] == d[-1] and d[-1] <= x:
                l.extend([d.pop(), d.popleft()])
            else:
                l.clear()
                break
        
T = int(input())
for i in range(T):
    n = int(input())
    l = list()
    d = deque(map(int, input().split()))
    can_stack(d, l)

    if len(l) > 0:
        print('Yes')
    else:
        print('No')
