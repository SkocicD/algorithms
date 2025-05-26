m = {'P': set(), 'K': set(), 'H': set(), 'T': set()}
for i in range(len(s := input()))[::3]:
    a, b, c = (s[i], s[i+1], s[i+2])
    n = int(b+c)
    if n in m[a]:
        print('GRESKA')
        exit()
    m[a].add(n)
print(*[13-len(m[k]) for k in m])
