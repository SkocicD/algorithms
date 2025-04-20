m, n = list(map(int, input().split()))
ct = 0
points = []
for r in range(m):
    for c, char in enumerate(input()):
        if char == '*':
            points.append((r+1, c+1))
            ct += 1
print(ct)
for r, c in points:
    print(r, c)
