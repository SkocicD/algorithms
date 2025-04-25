for _ in range(int(input())):
    n, a, b, c = list(map(int, input().split()))
    v = n//(a+b+c)
    n -= v*(a+b+c)
    if n == 0:
        print(3*v)
        continue
    if (n := n-a) <= 0:
        print(3*v+1)
        continue
    if (n := n-b) <= 0:
        print(3*v+2)
        continue
    if (n := n-c) <= 0:
        print(3*v+3)
        continue
