n, m = map(int, input().split())
welcome_line = n//2

for i in range(welcome_line):
    line_count = (2 * i) + 1
    dash_count = int((m - (line_count * 3))/2)
    print(''.join(['-'*dash_count, '.|.' * line_count, '-'*dash_count]))

dash_count = int((m - 7)//2) # line length - 'WELCOME'

print(''.join(['-'*dash_count, 'WELCOME', '-'*dash_count]))

for i in reversed(range(welcome_line)):
    line_count = (2 * i) + 1
    dash_count = int((m - (line_count * 3))/2)
    print(''.join(['-'*dash_count, '.|.' * line_count, '-'*dash_count]))