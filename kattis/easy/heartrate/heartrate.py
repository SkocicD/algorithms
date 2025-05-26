for _ in range(int(input())):
    b, p = list(map(float, input().split()))
    print(60*(b-1)/p, 60*b/p, 60*(b+1)/p)
