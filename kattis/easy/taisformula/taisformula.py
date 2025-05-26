total = 0
prev = None
curr = None
for _ in range(int(input())-1):
    if prev is None:
        prev = list(map(float, input().split()))
    else:
        prev = curr
    curr = list(map(float, input().split()))

    total += (prev[1] + curr[1])*(curr[0]-prev[0])/2000
print(total)
