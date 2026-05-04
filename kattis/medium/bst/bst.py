t = {}
c = 0
for _ in range(int(input())):
    n = int(input())
    ct = t
    d = 0
    while 'v' in ct:
        d += 1
        if n < ct['v']:
            ct = ct['lo']
        else:
            ct = ct['hi']
    ct['hi'] = {}
    ct['lo'] = {}
    ct['v'] = n
    ct['d'] = d
    c += d
    print(c)
