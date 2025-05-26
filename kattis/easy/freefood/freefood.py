days = set()
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    for x in range(a, b+1):
        days.add(x)
print(len(days))
