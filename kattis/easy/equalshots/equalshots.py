a, b = list(map(int, input().split()))
avg1, avg2 = (0, 0)
ct1, ct2 = (0, 0)
for _ in range(a):
    c, d = list(map(int, input().split()))
    avg1 += c*d
    ct1 += c
for _ in range(b):
    c, d = list(map(int, input().split()))
    avg2 += c*d
    ct2 += c
print('same' if avg1/ct1 == avg2/ct2 else 'different')
