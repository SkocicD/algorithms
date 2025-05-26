n, q = list(map(int, input().split()))
locs = list(map(int, input().split()))
for _ in range(q):
    a, b, c = list(map(int, input().split()))
    if a == 1:
        locs[b-1] = c
    else:
        print(abs(locs[b-1]-locs[c-1]))
