from math import asin, pi
for _ in range(int(input())):
    D, d, s = list(map(float, input().split()))
    print(int(pi/asin((d+s)/(D-d))))
