def works(combo):
    global people
    use(combo)
    for c in combo:
        if people[c] < 0:
            unuse(combo)
            return False
    return True


def unuse(combo):
    global people
    for c in combo:
        people[c] += 1


def use(combo):
    global people
    for c in combo:
        people[c] -= 1


def possible(minimum):
    global speeds
    global kayaks
    for kayak in kayaks:
        for speed in speeds:
            if speed[1]*kayak >= minimum and works(speed[0]):
                break
        else:
            return False
    return True


peoplecopy = {}
people = {}
for s, ct in zip(['b', 'n', 'e'], map(int, input().split())):
    peoplecopy[s] = ct
skillspeeds = list(zip(['b', 'n', 'e'], map(int, input().split())))

speeds = []
allowed = ['bb', 'bn', 'be', 'nn', 'ne', 'ee']
for ch, sp in skillspeeds:
    for chh, spp in skillspeeds:
        if ch+chh in allowed:
            speeds.append((ch+chh, sp + spp))

kayaks = sorted(map(int, input().split()))


hi = speeds[-1][1]*kayaks[-1]
lo = speeds[0][1]*kayaks[0]
while hi > lo:
    for k in peoplecopy:
        people[k] = peoplecopy[k]

    mid = (hi+lo+1)//2
    if possible(mid):
        lo = mid
    else:
        hi = mid - 1
print(lo)
