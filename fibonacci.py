cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    result = [0, 1]
    if n==0:
        return []
    elif n==1:
        return [0]
    
    for i in range(n-2):
        result.append(result[-1] + result[-2] )
    return result

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))