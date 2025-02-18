import math

d, s = [int(x) for x in input().split()]

def f(a):
    return a*math.cosh(d/(2*a))-a-s


tol = .000000000001
diff = 1
a,b = (d,1000)
while abs(a-b)>tol:
    c = (a+b)/2
    if f(a)*f(c)>0:
        a = c
    else:
        b = c

c = (a+b)/2
print(2*c*math.sinh(d/(2*c)))

