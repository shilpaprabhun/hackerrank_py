def print_formatted(number):
    spaces = len(bin(number).replace('0b', '')) + 1
    for i in range(1, number+1):
        oct1 = oct(i).replace('0o', '') 
        hex1 = hex(i).replace('0x', '').upper()
        bin1 = bin(i).replace('0b', '')
        response = ' '*(spaces - len(str(i)) - 1) + str(i) + ' '*(spaces - len(oct1)) + oct1 + ' '*(spaces - len(hex1)) + hex1 + ' '*(spaces - len(bin1)) + bin1
        
        print(response)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)