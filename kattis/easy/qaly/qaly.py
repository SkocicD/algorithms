from math import prod
total = 0
for _ in range(int(input())):
    total += prod(list(map(float, input().split())))
print(total)
