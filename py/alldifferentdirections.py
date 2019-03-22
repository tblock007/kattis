import sys
import math

def compute(x, y, inst):
    a = 0.0
    xx, yy = x, y
    for i in range(0, len(inst), 2):
        if inst[i] == 'start':
            a = float(inst[i + 1])
        elif inst[i] == 'walk':
            xx = xx + float(inst[i + 1]) * math.cos(a * math.pi / 180.0)
            yy = yy + float(inst[i + 1]) * math.sin(a * math.pi / 180.0)
        elif inst[i] == 'turn':
            a = (a + float(inst[i + 1])) % 360.0
    return (xx, yy)
    

while True:
    n = int(sys.stdin.readline())
    if (n == 0): break

    positions = []
    for i in range(n):
        words = sys.stdin.readline().split()
        x, y = float(words[0]), float(words[1])
        positions.append(compute(x, y, words[2:]))

    tx, ty = 0.0, 0.0
    for pos in positions:
        tx = tx + pos[0] / n
        ty = ty + pos[1] / n
    distances = [math.sqrt((pos[0] - tx)**2 + (pos[1] - ty)**2) for pos in positions]

    print('{0} {1} {2}'.format(tx, ty, max(distances)))
        
        
