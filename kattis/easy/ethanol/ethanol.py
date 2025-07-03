s = ['  H  ', '  -  ']
s += ['H|C|H', '  -  '] * int(input())
s += ['  O  ', '  H  ']
for w in zip(*s):
    print(''.join(w))
