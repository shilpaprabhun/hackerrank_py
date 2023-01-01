def merge_the_tools(string, k):
    # your code goes here
    l = len(string)
    for i in range(0, l, k):
        s = string[i:i+k]
        print("".join(list(dict.fromkeys(s))))
            

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)