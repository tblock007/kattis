from collections import namedtuple

class Box():
    def __init__(self, x1, y1, x2, y2, t):
        self.x1, self.y1, self.x2, self.y2, self.t = float(x1), float(y1), float(x2), float(y2), t

    def contains(self, x, y):
        return (x >= self.x1 and x <= self.x2 and y >= self.y1 and y <= self.y2)

    def is_match(self, t):
        return (t == self.t)



def status(peanut, boxes):
    for b in boxes:
        if b.contains(float(peanut[0]), float(peanut[1])):
            return 'correct' if b.is_match(peanut[2]) else b.t
    return 'floor'


first = True
while True:
    n = int(input())
    if n == 0:
        break
    if not first:
        print()
    else:
        first = False
    
    boxes = [Box(*input().split()) for i in range(n)]
    
    n = int(input())
    for i in range(n):
        line = input().split()
        print(line[2], status(line, boxes))
        

