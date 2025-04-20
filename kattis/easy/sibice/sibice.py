n, w, h = list(map(int, input().split()))
d = (w*w+h*h)**.5
for _ in range(n):
    print('DA' if int(input()) <= d else 'NE')
