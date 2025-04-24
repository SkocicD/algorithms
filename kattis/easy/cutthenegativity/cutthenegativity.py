ans = []
for r in range(int(input())):
    for c, val in enumerate(map(int, input().split())):
        if val > 0:
            ans.append((r+1, c+1, val))
print(len(ans))
for a in ans:
    print(*a)
