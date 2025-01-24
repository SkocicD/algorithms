t = int(input())

for _ in range(t):
    n = int(input())
    count = 1
    while (n-7) % 10 != 0 and n > 7:
        count += 1
        n -= 7
    if (n-7) % 10 == 0:
        print(count)
    elif n < 7:
        print(-1)

