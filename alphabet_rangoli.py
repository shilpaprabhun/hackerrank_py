def print_rangoli(size):
    width = (4 * size) - 3
    s=''
    i = size
    result =[]
    reverse = []
    cut = 0
    while i > 0 and i <= size:
        if i == size:
            s = chr(96+i)
        else:
            left_string = s[:len(s) - (2*cut)]
            s = left_string + '-' + chr(96+i) + '-' + left_string[::-1]
            cut+=1
        pad_len = (width - len(s))//2
        result.append(s.rjust(pad_len + len(s), '-').ljust(width, '-'))
        if i > 1:
            reverse.insert(0, s.rjust(pad_len + len(s), '-').ljust(width, '-'))
        i -= 1
    result.extend(reverse)
    print(*result, sep='\n')

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)