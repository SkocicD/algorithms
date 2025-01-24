
import math

n, k = [int(x) for x in input().split()]

ev = 0

for i in range(k):
    sum_over = 0
    
    if int(ev) < ev:
        start = int(ev) + 1
    else:
        start = ev
    
    for pip in range(start, n + 1):

        sum_over += pip

    ev = int(ev) * ev / n + sum_over / n

print(ev)
