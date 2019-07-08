import sys

# used to help sort pieces by type
rank = {'K':1, 'Q':2, 'R':3, 'B':4, 'N':5, 'P':6}

# we define a piece class that does all the work for us
# we only need to define how pieces should be compared
# as well as how a piece should be displayed; then we can 
# use built-in python functions in main to do the work
class piece:
    def __init__(self, p, r, c, color):
        self.p, self.r, self.c, self.color = p.upper(), r, c, color

    def __lt__(self, rhs):
        global rank
        if rank[self.p] != rank[rhs.p]:
            return (rank[self.p] < rank[rhs.p]) # if ranks are not equal, compare by rank
        if self.r != rhs.r:
            if self.color == 'b': # we assume that we will never try to sort pieces of different colors
                return (self.r > rhs.r) # if rows are not equal, compare by row
            else:
                return (self.r < rhs.r)
        return (self.c < rhs.c) # otherwise, compare by column

    def __str__(self):
        return '{0}{1}{2}'.format(self.p if self.p != 'P' else '', self.c, self.r) # defines how to create a string from the piece


# a helper function that picks out the appropriate cell in the board for us
# this is done because we can observe that most of the characters in the board 
# are actually irrelevant to this problem, and we can predict where the important 
# "piece-defining" characters are going to be
def extract(r, c, b):
    cc = ord(c) - ord('a')
    rr = 8 - r
    ri, ci = 2 * rr + 1, 4 * cc + 2
    if b[ri][ci] == '.' or b[ri][ci] == ':':
        return None
    else:
        return b[ri][ci]


white, black = [], [] # collects the pieces
b = [[c for c in line.strip()] for line in sys.stdin.readlines()] # read the input
rs = [1, 2, 3, 4, 5, 6, 7, 8]
cs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for r in rs:
    for c in cs:
        l = extract(r, c, b)
        if l:
            # if a piece is found on the square, append it to the appropriate list
            if l.isupper():
                white.append(piece(l, r, c, 'w'))
            else:
                black.append(piece(l, r, c, 'b'))
        
# a simple sort because we have defined __lt__ in our piece class
white.sort()
black.sort()

# print the output
print('White: {0}'.format(','.join(str(pp) for pp in white)))
print('Black: {0}'.format(','.join(str(pp) for pp in black)))
