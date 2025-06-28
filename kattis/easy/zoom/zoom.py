n, k = list(map(int, input().split()))
print(*list(m for i, m in enumerate(input().split()) if (i + 1) % k == 0))
