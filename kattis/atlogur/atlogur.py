import math
n = int(input())
knights = []
for i in range(n):
    h, s = input().split()
    knights.append([int(h), int(s), i + 1])

while len(knights) > 1:
    hits_to_kill_1 = math.ceil(knights[1][0] / knights[0][1])
    hits_to_kill_0 = math.ceil(knights[0][0] / knights[1][1])
    if hits_to_kill_1 <= hits_to_kill_0:
        knights[0][0] -= (hits_to_kill_1 - 1) * knights[1][1]
        knights.pop(1)
    else:
        knights[1][0] -= hits_to_kill_0 * knights[0][1]
        knights.pop(0)

print(knights[0][2]) 
