l, d, x = [int(input()) for i in '...']
first = None
last = None
for i in range(l, d+1):
    if sum(map(int, list(str(i)))) == x:
        last = i
        if first is None:
            first = i
print(first)
print(last)
