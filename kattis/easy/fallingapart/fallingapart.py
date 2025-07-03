input()
a, b, i = (0, 0, 0)
ns = list(map(int, input().split()))
while len(ns) > 0:
    if i % 2 == 0:
        a += max(ns)
    else:
        b += max(ns)
    ns.remove(max(ns))
    i += 1
print(a, b)
