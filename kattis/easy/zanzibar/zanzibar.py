from itertools import pairwise
for _ in range(int(input())):
    total = 0
    for a, b in pairwise(list(map(int, input().split()))):
        total += n if (n := b-2*a) > 0 else 0
    print(total)
