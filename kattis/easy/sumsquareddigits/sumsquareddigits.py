for _ in range(int(input())):
    tot = 0
    a, b, c = list(map(int, input().split()))
    while c > 0:
        m = c % b
        tot += m*m
        c = c//b
    print(a, tot)
