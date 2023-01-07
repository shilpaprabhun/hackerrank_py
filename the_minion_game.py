from itertools import combinations
from re import L
def minion_game(string):
    # your code goes here
    stuart = kevin = 0
    l = len(string)
    for i in range(l):
        if string[i] in 'AEIOU':
            kevin += l-i
        else:
            stuart += l-i

            
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")
 

if __name__ == '__main__':
    s = input()
    minion_game(s)