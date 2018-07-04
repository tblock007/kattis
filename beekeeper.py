def score(word):
    return word.count('aa') + word.count('ee') + word.count('ii') + word.count('oo') + word.count('uu') + word.count('yy')

while True:
    n = int(input())
    if n == 0:
        break

    words = [input() for i in range(n)]
    scores = [score(w) for w in words]
    print(words[scores.index(max(scores))])