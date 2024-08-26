import math

n, k = [int(x) for x in input().split()]

ev = 0

for i in range(k):

    start = math.floor(ev + 1)
    if start <= n:
        sum_over = (start + n)*(n - start + 1) / 2
    else:
        sum_over = 0
    
    ev = math.floor(ev) * ev / n + sum_over / n

print(ev)
