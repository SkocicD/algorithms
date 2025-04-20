from math import prod
c = float(input())
total = 0
for _ in range(int(input())):
    total += c*prod(map(float, input().split()))
print(total)
