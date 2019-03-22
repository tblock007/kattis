words = [w for w in input().split()]
unique_words = set(words)
print("yes" if len(words) == len(unique_words) else "no")