input()
teamcount = int(input())
problems = input().split()
totals = [0] * len(problems)
for _ in range(teamcount):
    for i, a in enumerate(map(int, input().split())):
        totals[i] += a
print(problems[totals.index(max(totals))])
