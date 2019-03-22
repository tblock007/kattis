class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return '{0} {1}'.format(int(self.x), int(self.y))

    def is_middle(self, c1, c2):
        return (self.x - c1.x) * (self.x - c2.x) + (self.y - c1.y) * (self.y - c2.y) < 1e-10

    def average(self, c1):
        return Point((self.x + c1.x) / 2, (self.y + c1.y) / 2)

    def mirror(self, mid):
        return Point((2 * mid.x - self.x), (2 * mid.y - self.y))

c = [Point(*[int(w) for w in input().split()]) for i in range(3)]
if c[0].is_middle(c[1], c[2]):
    mc, c1, c2 = c[0], c[1], c[2]
elif c[1].is_middle(c[0], c[2]):
    mc, c1, c2 = c[1], c[0], c[2]
elif c[2].is_middle(c[0], c[1]):
    mc, c1, c2 = c[2], c[0], c[1]
else:
    print('invalid input')

m = c1.average(c2)
print(mc.mirror(m))

