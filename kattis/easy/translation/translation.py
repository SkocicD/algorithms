input()
s = input().split()
d = {}
for _ in range(int(input())):
    a, b = input().split()
    d[a] = b
for w in s:
    print(d[w])
