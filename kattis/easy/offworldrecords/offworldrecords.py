n, c, p, t = list(map(int, input().split())) + [0]
for _ in range(n):
    if (k := int(input())) > c+p:
        t += 1
        p = c
        c = k
print(t)
