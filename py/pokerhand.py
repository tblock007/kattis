from collections import Counter

print(Counter([card[0] for card in input().split()]).most_common(1)[0][1])