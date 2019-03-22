import sys

def check(a, b, c):
    return (a + b == c) or (a * b == c) or (max(a, b) - min(a, b) == c) or (max(a, b) / min(a, b) == c)

sys.stdin.readline()
for line in sys.stdin.readlines():
    a, b, c = [int(num) for num in line.split()]
    print('Possible' if check(a, b, c) else 'Impossible')