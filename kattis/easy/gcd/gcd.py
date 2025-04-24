b, a = sorted(list(map(int, input().split())))
while a % b != 0:
    r = a % b
    a = b
    b = r
print(b)
