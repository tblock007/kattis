x = int(input())
y = int(input())

if (x > 0 and y > 0):
    print(1, end='')
elif (x > 0 and y < 0):
    print(4, end='')
elif (x < 0 and y > 0):
    print(2, end='')
else:
    print(3, end='')