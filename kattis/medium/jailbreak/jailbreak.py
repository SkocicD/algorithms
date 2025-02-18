class pos:
    def __init__(self,r,c,cost):
        global w
        global h
        self.p=r*w+c
        self.cost=cost
        self.adj=[r*w+c-1,r*w+c+1,(r-1)*w+c,(r+1)*w+c]
        self.isedge = (r==0 or c==0 or r==h-1 or c==w-1)
        self.prev=None


def get(fp,r,c):
    return fp[r][c] if r >= 0 and c >= 0 and r < len(fp) and c < len(fp[0]) else None
def left(r,c): return (r,c-1)
def right(r,c):
    return (r,c+1)
def above(r,c):
    return (r-1,c)
def below(r,c):
    return (r+1,c)
def printfp(fp):
    s = ''
    for r in fp:
        for c in r:
            s += c
        s+='\n'
    return s[:-1]



n = int(input())
for _ in range(n):
    h,w = list(map(int,input().split()))
    fp = [list(input()) for i in range(h)]
    adj = [[] for _ in range(h*w)]
    positions={}
    prisoners=[]
    exits=set()
    for r in range(h):
        for c in range(w):
            if fp[r][c] in '.$#':
                match(fp[r][c]):
                    case '.':
                        p=pos(r,c,0)
                    case '$':
                        p=pos(r,c,0)
                        prisoners.append(p.p)
                    case '#':
                        p=pos(r,c,1)
                positions[p.p]=p
    # TODO: Now iterate over the positions and do work with their neighbors. Maybe move the left,right,etc into the class
    for p in positions:
        i=0
        while i < len(positions[p].adj):
            if positions[p].adj[i] in positions:
                positions[p].adj[i] = positions[positions[p].adj[i]]
                i+=1
            else:
                positions[p].adj.pop(i)
        
    # dijkstra's alg
    prev = [-1 for _ in range(w*h)]
    costs = [0 for _ in range(w*h)]

    nexts=[prisoners[0]]
    visited=set()

    while len(nexts)!=0:
        curr=positions[nexts.pop(0)]
        for node in curr.adj:
            if node.p not in visited:
                node.cost=curr.cost+node.cost
                for i,p in enumerate(nexts):
                    if costs[p]>costs[pos]:
                        nexts.insert(i,node.p)
                        break
                else:
                    nexts.append(node.p)
                node.prev=curr

        visited.add(curr)

    s = ''
    for r in range(h):
        for c in range(w):
            s+='.' if costs[r*w+c] ==99999 else str(costs[r*w+c])
        s+='\n'
    print(s[:-1])

