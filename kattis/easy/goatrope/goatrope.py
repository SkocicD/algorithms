x, y, x1, y1, x2, y2 = list(map(int, input().split()))
if x1 < x and x < x2:
    print(min(abs(y-y1), abs(y-y2)))
    exit()
if y1 < y and y < y2:
    print(min(abs(x-x1), abs(x-x2)))
    exit()
print((min(abs(y-y1), abs(y-y2)) ** 2 + min(abs(x-x1), abs(x-x2)) ** 2) ** .5)
