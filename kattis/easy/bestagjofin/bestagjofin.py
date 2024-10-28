n = int(input())
d = {}
for _ in range(n):
    a,b = input().split()
    d[a] = int(b)

print(max(d,key=d.get))
