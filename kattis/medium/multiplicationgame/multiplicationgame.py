import math
from functools import cache
from collections import Counter
primes = []
for i in range(2, math.ceil(math.sqrt((2<<31)-1))):
    prime = True
    for p in primes:
        if i % p == 0:
            prime = False
            break
    if prime:
        primes.append(i)

@cache
def prime_factorize(n):
    f = []
    if n == 1:
        return f
    for p in primes:
        if n % p == 0:
            f.append(p)
            f += prime_factorize(n//p)
            return f
    return [n]

t = int(input())

s = ''
for _ in range(t):
    n, a = input().split()
    other = 'Bob' if a == 'Alice' else 'Alice'
    n = int(n)
    factorization = prime_factorize(n)
    factors = dict(Counter(factorization))

    if len(factors) > 2:
        s+='tie\n'
    elif len(factors) == 1:
        s += a+'\n' if factors[factorization[0]]%2 == 1 else other+'\n'
    else:
        m,n = factors.values()
        if abs(m-n) == 0: 
            s+=other+'\n'
        elif abs(m-n) == 1:
            s+=a+'\n'
        else:
            s+='tie\n'

print(s[:-1])
