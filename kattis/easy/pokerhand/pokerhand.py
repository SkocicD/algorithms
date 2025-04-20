from collections import Counter
print(max(Counter([s[0] for s in input().split()]).values()))
