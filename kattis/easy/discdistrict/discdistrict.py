import math
r = int(input())
r_sq = r*r
min = 1 

for x in range(r+1):
    y = math.sqrt(r_sq - x*x)
    y = (int(y) + 1 if y==int(y) else math.ceil(y))
    dist = math.sqrt(x*x+y*y)
    if dist-r < min:
        min = dist - r
        minxy = (x,y)

x, y = minxy
print(f'{x} {y}')
