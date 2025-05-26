from math import sin, pi, ceil
a, b = list(map(int, input().split()))
print(ceil(a/sin(b/180*pi)))
