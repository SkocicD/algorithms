counts = [0]*3
for _ in range(int(input())):
    for i, v in enumerate(input().split()):
        counts[i] += 1 if v == 'J' else 0

print(min(counts))
