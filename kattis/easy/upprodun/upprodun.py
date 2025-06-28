from math import ceil
n = int(input())
m = int(input())

strings = ['*' * (m//n)]*n


for i in range(m-n*(m//n)):
    strings[i] += '*'

[print(s) for s in strings]
