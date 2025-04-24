n, m, k = list(map(int, input().split()))
arr = ['.'*m]*n
for _ in range(k):
    a, b = list(map(int, input().split()))
    s = arr[a-1]
    arr[a-1] = s[0:b-1]+'*'+s[b:]
[print(r) for r in arr]
