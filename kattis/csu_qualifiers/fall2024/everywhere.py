n = int(input())

for _ in range(n):
    a = int(input())
    s = set()
    for __ in range(a):
        s.add(input())
    print(len(s))
