def get_count(s):
    unique_characters = set(s)
    d = dict()
    for x in unique_characters:
        c = s.count(x)
        d[c] = ' '.join([x, d.get(c, '')])
    
    keys = list(d.keys()).copy()
    keys.sort()
    
    sorted_dict = {i: d[i] for i in keys}

    cnt = 0
    index = 0
    while cnt < 3:
        t = sorted_dict.popitem()
        index += 1
        chars = t[-1].split()
        chars.sort()
        for c in chars:
            print(c, t[0])
            cnt += 1
            if cnt == 3:
                break   

if __name__ == '__main__':
    s = input()
    get_count(s)
