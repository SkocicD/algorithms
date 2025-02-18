from math import sinh, cosh

d, s = [int(x) for x in input().split()]

def f(a):
    return a*cosh(d/(2*a))-a-s

a,b=(1,1)
while f(a)<0 or f(b)>0:
    a/=2 if f(a)<0 else a 
    b*=2 if f(b)>0 else b

prevc = -1
c = (a+b)/2
while abs(1-c/prevc)>.00000000001:
    if f(a)*f(c)>0:
        a = c
    else:
        b = c
    prevc = c
    c = (a+b)/2

print(2*c*sinh(d/(2*c)))

