from statistics import median
a, m = ([], [])
for _ in range(4):
    m.append(list(map(int, input().split())))
for z in zip(*m[1:]):
    a.append(median(z))
print(*a)
