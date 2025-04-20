n, k = list(map(int, input().split()))
s = sum([int(input()) for _ in range(k)])
print((s-3*(n-k))/n, (s+3*(n-k))/n)
