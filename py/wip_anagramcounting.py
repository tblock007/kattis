import sys

def tochar(i):
    if i >= 0 and i <= 25:
        return chr(i + ord('a'))
    if i >= 26 and i <= 51:
        return chr(i + ord('A') - 26)

class charcounts:
    def __init__(self):
        self.remaining = 0
        self.counts = [0 for i in range(52)]

    def at(self, index):
        return self.counts[index]

    def add(self, c):
        if (ord(c) >= ord('a') and ord(c) <= ord('z')):
            self.counts[ord(c) - ord('a')] += 1
            self.remaining += 1
        if (ord(c) >= ord('A') and ord(c) <= ord('Z')):
            self.counts[ord(c) - ord('A') + 26] += 1
            self.remaining += 1

    def remove(self, c):
        if (ord(c) >= ord('a') and ord(c) <= ord('z')):
            self.counts[ord(c) - ord('a')] -= 1
            self.remaining -= 1
        if (ord(c) >= ord('A') and ord(c) <= ord('Z')):
            self.counts[ord(c) - ord('A') + 26] -= 1
            self.remaining -= 1

    def print(self):
        print(self.counts)

    def tostring(self):
        fakechars = sorted(self.counts)
        result = ''
        i = len(fakechars) - 1
        while fakechars[i] > 0:
            result += ''.join(tochar(i) for j in range(fakechars[i]))
            i -= 1
        return result


def compute(cc, memo):
    if (cc.remaining == 0):
        return 1
    if cc.tostring() in memo.keys():
        return memo[cc.tostring()]

    sum = 0
    for i in range(52):
        if (cc.at(i) > 0):
            cc.remove(tochar(i))
            sum += compute(cc, memo)
            cc.add(tochar(i))
    memo[cc.tostring()] = sum
    return sum


for line in sys.stdin.readlines():
    cc = charcounts()
    memo = dict()
    for c in line:
        cc.add(c)
    print(compute(cc, memo))
    #print(cc.tostring())
