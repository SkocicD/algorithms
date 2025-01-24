from itertools import pairwise

d = {}
n,k = [int(x) for x in input().split()]
pools = [{x+1,} for x in range(n)]

for _ in range(k):
    # print(pools)
    ai, bi = [int(x) for x in input().split()]
    if bi in pools[ai-1]:
        continue
    p1,p2 = (pools[ai-1],pools[bi-1]) if len(pools[ai-1]) > len(pools[bi-1]) else (pools[bi-1],pools[ai-1])
    # print(f'{p1} {p2}')
    p1.update(p2)
    for m in p2:
        pools[m-1] = p1

# print(pools)
          
for i, pool in enumerate(pools):
    if n-i not in pool:
        print('no')
        exit()
print('yes')
