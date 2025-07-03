a, b = list(map(int, input().split()))
b = ['']*b
inp = [input() for _ in range(a)]
for i, w in enumerate(zip(*inp)):
    b[i] = 'S' * ''.join(w).count('S')
    b[i] = '.' * (a-len(b[i])) + b[i]
for w in zip(*b):
    print(''.join(w))
