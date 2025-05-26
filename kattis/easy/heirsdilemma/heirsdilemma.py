a, b = list(map(int, input().split()))
tot = 0
for c in range(a, b+1):
    s = set(str(c))
    if len(s) < 6:
        continue
    if '0' in s:
        continue
    for d in s:
        if c % int(d) != 0:
            break
    else:
        tot += 1
print(tot)
