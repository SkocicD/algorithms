def next(total, prev, rest):
    global mn
    global quickchanges

    if total > mn:
        return
    if len(rest) == 0:
        mn = min(total, mn)
        return
    for i in range(len(rest)):
        other = rest.pop(i)
        if prev != -1:
            next(total + quickchanges[prev][other], other, rest)
        else:
            next(total, other, rest)
        rest.insert(i, other)


dances = []
for _ in range(n := int(input())):
    dances.append(set(input()))

quickchanges = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        quickchanges[i][j] = len(dances[i].intersection(dances[j]))
        quickchanges[j][i] = quickchanges[i][j]


mn = 9999999999999999

next(0, -1, [i for i in range(n)])
print(mn)
