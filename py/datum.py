d,m = [int(n) for n in input().split()]
mo = [6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
y = 4
c = 0
r = (d + mo[m - 1] + y + c) % 7
dotw = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print(dotw[r])