s, t, n = list(map(int, input().split()))
d = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

for i in range(n):
    s += d[i]
    if s % c[i] != 0:
        s += c[i] - (s % c[i])
    s += b[i]
s += d[-1]
print('yes' if s <= t else 'no')
