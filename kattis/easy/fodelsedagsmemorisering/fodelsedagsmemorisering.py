d = {}
for _ in range(int(input())):
    n, c, bd = input().split()
    c = int(c)
    if bd in d:
        if d[bd][1] < c:
            d[bd] = (n, c)
    else:
        d[bd] = (n, c)
names = []
for bd in d:
    names.append(d[bd][0])
print(len(names))
[print(name) for name in sorted(names)]
