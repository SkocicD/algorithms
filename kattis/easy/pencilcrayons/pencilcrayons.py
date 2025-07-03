a, b = list(map(int, input().split()))
tot = 0
for _ in range(a):
    l = input().split()
    tot += len(l) - len(set(l))
print(tot)
