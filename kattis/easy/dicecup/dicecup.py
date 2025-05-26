n, m = list(map(int, input().split()))
ways = [0]*(n+m)
for i in range(1, n+1):
    for j in range(1, m+1):
        ways[i+j-1] += 1
m = max(ways)
[print(i+1) for i in range(len(ways)) if ways[i] == m]
