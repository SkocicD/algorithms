from collections import defaultdict

class rook:
    def __init__(self,r,c,x):
        self.r = r
        self.c = c
        self.x = x

    def __eq__(self,other):
        return self.r == other.r and self.c == other.c

    def __hash__(self):
        return hash((self.r, self.c))

def getattacked():
    a = 0
    for rk in rooks:
        for other in cols[rk.c]:
            if other == rk:
                continue
            a = a ^ other.x
        for other in rows[rk.r]:
            if other == rk:
                continue
            a = a ^ other.x
        print(a)

n,k,p = list(map(int,input().split()))

rooks = {}
rows = defaultdict(set)
cols = defaultdict(set)
for i in range(k):
    rk = rook(*tuple(map(int,input().split())))
    rooks[rk] = rk
    cols[rk.c].add(rk)
    rows[rk.r].add(rk)

for i in range(p):
    r1,c1,r2,c2 = list(map(int,input().split()))
    rk = rooks[rook(r1,c1,0)]
    cols[rk.c].remove(rk)
    rows[rk.r].remove(rk)
    rk.r = r2
    rk.c = c2
    cols[rk.c].add(rk)
    rows[rk.r].add(rk)
    getattacked()
