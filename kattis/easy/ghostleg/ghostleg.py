n, m = list(map(int, input().split()))
g = [[-1]*m for _ in range(n)]
for i in range(m):
    a = int(input())
    g[a-1][i] = a
    g[a][i] = a-1

ans = [-1] * n
for i in range(n):
    a = i
    for j in range(m):
        if g[a][j] != -1:
            a = g[a][j]
    ans[a] = i
[print(i+1) for i in ans]
