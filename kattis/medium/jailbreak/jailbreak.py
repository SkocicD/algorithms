def get(fp,r,c):
    return fp[r][c] if r >= 0 and c >= 0 and r < len(fp) and c < len(fp[0]) else None
def left(r,c):
    return (r,c-1)
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
    start,end=(None,None)
    for r in range(h):
        for c in range(w):
            if fp[r][c] in '.$#':
                for fun in [left,right,above,below]:
                    rr,cc = fun(r,c)
                    match(get(fp,rr,cc)):
                        case '$':
                            if start is None:
                                start=rr*w+cc
                            else:
                                end=rr*w*cc;
                            adj[r*w+c].append((rr*w+cc,0))
                        case '.':
                            adj[r*w+c].append((rr*w+cc,0))
                        case '#':
                            adj[r*w+c].append((rr*w+cc,1))

    # dijkstra's alg
    prev = [-1 for _ in range(w*h)]
    costs = [99999 for _ in range(w*h)]
    nexts=[]
    visited=set()

    curr=start
    costs[curr]=0
    while curr is not None:
        for node in adj[curr]:
            pos,cost=node
            if pos not in visited:
                costs[pos]=costs[curr]+cost
                for i,p in enumerate(nexts):
                    if costs[p]>costs[pos]:
                        nexts.insert(i,pos)
                        break
                else:
                    nexts.append(pos)
                prev[pos]=curr
        visited.add(curr)
        curr=nexts.pop(0) if len(nexts)>0 else None
        
    print(len(visited))
    s = ''
    for r in range(h):
        for c in range(w):
            s += '.' if costs[r*w+c] == 99999 else str(costs[r*w+c])
        s+='\n'
    print(s[:-1])



