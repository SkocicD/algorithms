n, q = list(map(int, input().split()))
m = {}
for _ in range(n):
    f, l = input().split()
    if (s := f[0]+l[0]) not in m:
        m[s] = [(f, l)]
    else:
        m[s].append((f, l))
for _ in range(q):
    if (s := input()) not in m:
        print('nobody')
    elif len(m[s]) > 1:
        print('ambiguous')
    else:
        print(*m[s][0])
