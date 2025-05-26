n = int(input())
print(n)
m = {}
while (s := input()) != '-1':
    s = list(map(int, s.split()))
    for x in s[1:]:
        m[x] = s[0]
while n in m:
    n = m[n]
    print(n)
