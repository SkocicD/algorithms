import math

d, s = [int(x) for x in input().split()]
lower = 0
upper = 1000

rhs = math.e + 1/math.e

while upper - lower > .000001:
    a = lower + (upper - lower)/2
    print(a)
    guess = 2 * (a + s) / a * math.e ** (2*a/d)
    print(guess)
    if guess >= rhs:
        upper = a
    else:
        lower = a

print(a)
print(2 * a * math.sinh(d/(2*a)))
