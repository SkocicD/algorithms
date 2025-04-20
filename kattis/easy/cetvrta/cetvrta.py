from collections import Counter
a1, b1 = list(map(int, input().split()))
a2, b2 = list(map(int, input().split()))
a3, b3 = list(map(int, input().split()))
c1 = Counter([a1, a2, a3])
c2 = Counter([b1, b2, b3])
for k in c1:
    if c1[k] == 1:
        x = k
for k in c2:
    if c2[k] == 1:
        y = k
print(x, y)
