def calc(t, x):
    a, b = t
    return a*x+b


def dist_at(x):
    global lines
    lo, hi = (1e8, -1e8)
    for line in lines:
        lo = min(lo, calc(line, x))
        hi = max(hi, calc(line, x))
    return (hi-lo)


lines = []
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    lines.append((b, a))

lo = 0
hi = 1000
d = dist_at(lo)

while hi-lo > 1e-4:
    mid = (hi+lo)/2
    midl = mid-.001
    midr = mid+.001
    distl = dist_at(midl)
    dist = dist_at(mid)
    distr = dist_at(midr)
    if distl > dist and dist < distr:
        break
    elif dist > distr:
        lo = mid
    else:
        hi = mid
print(dist_at(mid))
