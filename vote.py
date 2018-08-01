t = int(input())
for cas in range(t):
    n = int(input())
    votes = [int(input()) for ii in range(n)]
    m = max(votes)
    s = sum(votes)
    if (votes.count(m) > 1):
        print('no winner')
    else:
        winner = votes.index(m) + 1
        if (2 * m) > s:
            print('majority winner', winner)
        else:
            print('minority winner', winner)