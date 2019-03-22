while True:
    x, y = [int(w) for w in input().split()]
    if (x == 0 and y == 0):
        break
    if (x + y == 13):
        print('Never speak again.')
    elif (x > y):
        print('To the convention.')
    elif (x < y):
        print('Left beehind.')
    else:
        print('Undecided.')