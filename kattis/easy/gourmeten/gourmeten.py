mins = int(input())
meals = []
for _ in range(int(input())):
    meals.append(int(input()))

times = [1] + [0] * mins
for m in range(mins):
    for t in meals:
        if m + t < len(times):
            times[m+t] += times[m]
print(times[-1])
