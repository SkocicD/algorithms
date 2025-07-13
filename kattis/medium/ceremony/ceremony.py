from bisect import bisect_right
input()
h = sorted(map(int, input().split()))

total = 0
last = len(h)
cut = 0
low = 0
while last - low > 0:
    # find the index that is the number of buildings (last-low) plus how many floors have been cut off of it (+cut)
    # add cut because if there are 4 buildings left and they all had 2 cut off, we need some that were originally 6 (4+2)
    i = bisect_right(h, last-low+cut, hi=last)
    # if there exist any towers taller than the number ofbuildings left, add this number of buildings to the total
    if i < last:
        total += last-i
        last = i
    else:
        cut += 1
        total += 1
        low = bisect_right(h, cut)
print(total)
