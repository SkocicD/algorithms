from collections import defaultdict

n,k = list(map(int,input().split()))

ppl = defaultdict(set)

for j in range(n):
    a,b = list(map(int,input().split()))
    for i in range(a,b):
        ppl[i].add(j)

for val in ppl:
    print(ppl[val])
