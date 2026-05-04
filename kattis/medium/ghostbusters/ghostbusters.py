from collections import defaultdict
points = []
xlines = defaultdict(list)
ylines = defaultdict(list)
for _ in range(int(input())):
    pt = list(map(int, input().split()))
    xlines[pt[0]].append(pt)
    ylines[pt[1]].append(pt)
for xline in xlines:
    xlines[xline] = sorted(xlines[xline], key=lambda x: x[1])
for yline in ylines:
    ylines[yline] = sorted(ylines[yline], key=lambda x: x[0])

print(xlines)
print(ylines)
