r, c = list(map(int, input().split()))
arr = [list(input()) for _ in range(r)]
totals = [0]*5
for rr in range(r-1):
    for cc in range(c-1):
        squares = [arr[rr][cc], arr[rr+1][cc], arr[rr][cc+1], arr[rr+1][cc+1]]
        numcars = sum(1 for s in squares if s == 'X')
        if "#" in squares:
            continue
        else:
            totals[numcars] += 1
[print(x) for x in totals]
