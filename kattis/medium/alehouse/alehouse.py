from bisect import bisect_right, bisect_left
n, k = list(map(int, input().split()))

starts = []
ends = []
all = []

for j in range(n):
    a, b = list(map(int, input().split()))
    starts.append(a)
    ends.append(b)
    all.append(a)
    all.append(b)

starts = sorted(starts)
ends = sorted(ends)
mx = 0
# find the number of ranges that start before its endpoint and subtract the number that end before its start point
for i in range(2*n):
    high = all[i]
    low = high - k
    a = bisect_right(starts, high)  # number that start before the end point
    b = bisect_left(ends, low)  # number that end before the start point
    mx = max(mx, a-b)
print(mx)
