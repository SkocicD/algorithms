n = int(input())
for _ in range(n):
    a = int(input())
    d = {}
    for __ in range(a):
        x,y = input().split()
        if y not in d:
            d[y] = set()
        d[y].add(x)
    base = 2**len(d)
    total = base
    for key in d:
        total += (base / 2) * (len(d[key]) - 1)
        base += (base / 2) * (len(d[key]) - 1)
    print(int(total) - 1)
