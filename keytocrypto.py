def sv(c):
    return ord(c) - ord('A')

def shift(c, s):
    val = ord(c) - sv(s)
    if val < ord('A'):
        val += 26
    return chr(val)

cipher = input()
key = input()
decoded = ''
for i in range(len(cipher)):
    decoded += shift(cipher[i], key[i])
    key += decoded[i]
print(decoded)