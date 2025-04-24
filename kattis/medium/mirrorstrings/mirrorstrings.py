def below(n):
    m = n//2+1
    return 5**m//2 + 2*2**m - 6 + (5**m+2**m if n % 2 == 1 else 0)


l, r = list(map(int, input().split()))
print((below(r)-below(l-1)) % 1000000007)
