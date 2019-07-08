# we will determine how long the cycle is by tracking ONLY the second card
# some math reveals that this is sufficient for determining the cycle length
# i.e., when the second card returns to its original position, all other 
# cards will also be in their original positions
def cycle(n, st):
    steps = 1
    i = track(2, n, st)
    while i != 2:
        steps += 1
        i = track(i, n, st)
    return steps


# performs the tracking of an individual card
# there are four cases: in with odd number, in with even number, 
# out with odd number, and out with even number
# but we can easily compute where a given card will end up 
# in each case
def track(i, n, st):
    if st == "out":        
        i -= 1 # use zero-indexing
        if i < (n / 2):
            return (i * 2) + 1 # resulting slot for this card, returned to one-based indexing
        else:
            j = (n - i - 1) if n % 2 == 0 else (n - i) # convert to a "reverse index", which depends on parity of n
            j *= 2 # perform the shuffle for this card in reverse indexing
            return (n - j) if n % 2 == 0 else (n - j + 1) # this returns it to non-reverse one-based indexing
    elif st == "in":
        if i <= (n / 2):
            return (i * 2)
        else:
            j = (n - i + 1) if n % 2 == 0 else (n - i)
            j *= 2
            return (n - j + 1) if n % 2 == 0 else (n - j)


nn, st = input().split()
n = int(nn)

# handle the special case of a one-card deck, for which the methodology 
# will not work
if n == 1:
    print(1)
else:
    print(cycle(n, st))
