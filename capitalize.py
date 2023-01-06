#!/bin/python3

import os


# Complete the solve function below.
def solve(s):
    l = s.split(' ')
    result= ''
    for item in l:
        result += item.capitalize() + ' '
        
    return result.rstrip()
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
