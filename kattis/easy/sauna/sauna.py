l, h = (0, 999999999)
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    if a > l:
        l = a
    if b < h:
        h = b
print(f'{h-l+1} {l}' if l <= h else 'bad news')
