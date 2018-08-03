def parse(digit):
    if (digit == '**** ** ** ****'):
        return '0'
    if (digit == '  *  *  *  *  *'):
        return '1'
    if (digit == '***  *****  ***'):
        return '2'
    if (digit == '***  ****  ****'):
        return '3'
    if (digit == '* ** ****  *  *'):
        return '4'
    if (digit == '****  ***  ****'):
        return '5'
    if (digit == '****  **** ****'):
        return '6'
    if (digit == '***  *  *  *  *'):
        return '7'
    if (digit == '**** ***** ****'):
        return '8'
    if (digit == '**** ****  ****'):
        return '9'
    return '*'
    
    
    

grid = [list(input()) for i in range(5)]
num_string = ''
for j in range(0, len(grid[0]), 4):
    digit = ''.join([''.join(grid[i][j:j + 3]) for i in range(5)])
    num_string = num_string + parse(digit)
if '*' in num_string:
    print('BOOM!!')
else:
    if int(num_string) % 6 == 0:
        print('BEER!!')
    else:
        print('BOOM!!')
