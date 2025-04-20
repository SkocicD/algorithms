l, x = list(map(int, input().split()))
count, total = (0, 0)
for _ in range(x):
    enter, p = input().split()
    p = int(p)
    if enter == 'leave':
        p = -p
    if total+p <= l:
        total += p
    else:
        count += 1
print(count)
