from itertools import pairwise
pp = []
for _ in range(int(input())):
    pp.append(tuple(map(int, input().split())))
m = 0
for pp1, pp2 in pairwise(pp):
    m = max(m, (pp2[1]-pp1[1])//(pp2[0]-pp1[0]))
print(m)
