total = 0
m = 0
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    total = total-a+b
    m = max(total, m)
print(m)
