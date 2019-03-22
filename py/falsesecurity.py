import sys

def tm(s):
    if s == 'A': return '.-'
    if s == 'B': return '-...'
    if s == 'C': return '-.-.'
    if s == 'D': return '-..'
    if s == 'E': return '.'
    if s == 'F': return '..-.'
    if s == 'G': return '--.'
    if s == 'H': return '....'
    if s == 'I': return '..'
    if s == 'J': return '.---'
    if s == 'K': return '-.-'
    if s == 'L': return '.-..'
    if s == 'M': return '--'
    if s == 'N': return '-.'
    if s == 'O': return '---'
    if s == 'P': return '.--.'
    if s == 'Q': return '--.-'
    if s == 'R': return '.-.'
    if s == 'S': return '...'
    if s == 'T': return '-'
    if s == 'U': return '..-'
    if s == 'V': return '...-'
    if s == 'W': return '.--'
    if s == 'X': return '-..-'
    if s == 'Y': return '-.--'
    if s == 'Z': return '--..'
    if s == '_': return '..--'
    if s == '.': return '---.'
    if s == ',': return '.-.-'
    if s == '?': return '----'

def tc(s):
    if s == '.-': return 'A'
    if s == '-...': return 'B'
    if s == '-.-.': return 'C'
    if s == '-..': return 'D'
    if s == '.': return 'E'
    if s == '..-.': return 'F'
    if s == '--.': return 'G'
    if s == '....': return 'H'
    if s == '..': return 'I'
    if s == '.---': return 'J'
    if s == '-.-': return 'K'
    if s == '.-..': return 'L'
    if s == '--': return 'M'
    if s == '-.': return 'N'
    if s == '---': return 'O'
    if s == '.--.': return 'P'
    if s == '--.-': return 'Q'
    if s == '.-.': return 'R'
    if s == '...': return 'S'
    if s == '-': return 'T'
    if s == '..-': return 'U'
    if s == '...-': return 'V'
    if s == '.--': return 'W'
    if s == '-..-': return 'X'
    if s == '-.--': return 'Y'
    if s == '--..': return 'Z'
    if s == '..--': return '_'
    if s == '---.': return '.'
    if s == '.-.-': return ','
    if s == '----': return '?'

for line in sys.stdin.readlines():
    morse = ''.join(tm(c) for c in line.strip())
    l = [len(tm(c)) for c in line.strip()]
    l.reverse()
    index = 0
    decoded = []
    for i in l:
        decoded.append(tc(morse[index:index + i]))
        index = index + i
    print(''.join(decoded))
