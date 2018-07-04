line = input()
ball = 1
for c in line:
    if c == 'A':
        if ball == 1: ball = 2
        elif ball == 2: ball = 1
    elif c == 'B':
        if ball == 2: ball = 3
        elif ball == 3: ball = 2
    elif c == 'C':
        if ball == 1: ball = 3
        elif ball == 3: ball = 1
print(ball)