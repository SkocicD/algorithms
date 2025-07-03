mn = 9999999999999999999999999999
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    if b == 0:
        mn = min(a, mn)
print(mn if mn < 9999999999999999999999999999 else -1)
