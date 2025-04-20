ct = 0
for _ in range(int(input())):
    if 'pink' in (s := input().lower()) or 'rose' in s:
        ct += 1
print(ct if ct > 0 else 'I must watch Star Wars with my daughter')
