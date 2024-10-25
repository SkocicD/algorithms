d = {}
for _ in range(int(input())):
    l = input().split()
    if l[2] not in d:
        d[l[2]] = set()
    d[l[2]].add((l[0],l[1]))
[print(f'{c} {len(d[c])}') for c in sorted(d)]
