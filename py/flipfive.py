from collections import deque

# number the board as follows:
#
# 0 1 2
# 3 4 5
# 6 7 8
#
# then this list of lists gives the positions that should be flipped if a given position is clicked
flips = [[0, 1, 3], [0, 1, 2, 4], [1, 2, 5], [0, 3, 4, 6], [1, 3, 4, 5, 7], [2, 4, 5, 8], [3, 6, 7], [4, 6, 7, 8], [5, 7, 8]]


# performs the flip and returns the new board after the click
def flip(board, pos):
    global flips
    result = [c for c in board]
    for f in flips[pos]:
        result[f] = '*' if result[f] == '.' else '.'
    return ''.join(result)


# performs a BFS on the implicit graph in order to determine the 
# minimum number of moves
def movesToSolve(board):

    # handle the special case that a board is already complete
    if board == ".........":
        return 0

    # tracks which boards we've seen already
    visited = set()

    # a queue that stores the next boards to examine
    # this queue will also store the number of steps to reach this board 
    # so that we can track how far along we are in the process
    q = deque()

    # initialize the queue with the initial board, as well as a 0 to indicate
    # that there are zero steps
    q.append((board, 0))
    visited.add(board)

    # the meat of the BFS - as long as the queue is not empty, process the 
    # next board state and add all of its "neighbors" to the queue
    # here, a "neighbor" of a board is one that can be reached in one click
    while q:
        # bring out the next board state and the number of steps needed 
        # to reach it
        curr, n = q.popleft()
        
        # try every move
        for move in range(9):
            next = flip(curr, move)

            # the exit condition - once we reach this state we can 
            # return the number of steps needed to reach it
            if next == ".........":
                return (n + 1)

            # note that we only add neighbors if it hasn't been seen 
            # before - this is important, so that we do not end up 
            # examining a board more than once
            if next not in visited:
                visited.add(next)
                q.append((next, n + 1))



n = int(input())
for _ in range(n):
    b = input() + input() + input()
    print(movesToSolve(b))