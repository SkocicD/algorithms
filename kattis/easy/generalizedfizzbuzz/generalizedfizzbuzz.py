n, a, c, f, b, fb = list(map(int, input().split())) + [0, 0, 0]
for i in range(1, n+1):
    if i % a == 0 and i % c == 0:
        fb += 1
    elif i % a == 0:
        f += 1
    elif i % c == 0:
        b += 1
print(*[f, b, fb])
