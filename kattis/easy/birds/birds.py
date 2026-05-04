from itertools import pairwise
l, d, n = list(map(int, input().split()))
l += 2*d - 12
birds = [int(input())-6 for _ in range(n)]
print(sum((b-a-d)//d for a, b in pairwise(sorted(birds+[0, l]))))
