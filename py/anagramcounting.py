import sys
import math

def tochar(i):
    if i >= 0 and i <= 25:
        return chr(i + ord('a'))
    if i >= 26 and i <= 51:
        return chr(i + ord('A') - 26)

class charcounts:
    def __init__(self):
        self.remaining = 0
        self.counts = [0 for i in range(52)]

    def add(self, c):
        if (ord(c) >= ord('a') and ord(c) <= ord('z')):
            self.counts[ord(c) - ord('a')] += 1
            self.remaining += 1
        if (ord(c) >= ord('A') and ord(c) <= ord('Z')):
            self.counts[ord(c) - ord('A') + 26] += 1
            self.remaining += 1

    def solve(self):
        ans = math.factorial(self.remaining)
        for count in self.counts:
            ans = ans // math.factorial(count)
        return ans



for line in sys.stdin.readlines():
    cc = charcounts()
    for c in line:
        cc.add(c)
    print(cc.solve())
