import heapq


def ngbrs(s):
    global rows
    global cols
    global board

    r, c = s
    nbs = set()
    if r > 0:
        nbs.add((r-1, c))
    if r < rows-1:
        nbs.add((r+1, c))
    if c > 0:
        nbs.add((r, c-1))
    if c < cols-1:
        nbs.add((r, c+1))
    return nbs


def get(s):
    global board
    r, c = s
    return board[r][c]


def one_d(s):
    global cols
    r, c = s
    return r*cols + c


def reqladder(s1, s2):
    a = get(s2)-get(s1)
    return a if a > 0 else 0


def printvisited():
    global visited
    global board
    global rows
    global cols

    for r in range(rows):
        col = ['X' if x else '.' for x in visited[r*cols:r*cols+cols]]
        print(*col)


rows, cols = list(map(int, input().split()))
board = [list(map(int, input().split())) for row in range(rows)]

visited = [False for _ in range(rows*cols)]
ladders = [99999999 for _ in range(rows*cols)]
ladders[0] = 0
q = [(0, (0, 0))]

while not visited[one_d((rows-1, cols-1))]:
    currlad, curr = heapq.heappop(q)
    for nb in ngbrs(curr):
        if not visited[one_d(nb)]:
            ladders[one_d(nb)] = max(ladders[one_d(curr)], reqladder(curr, nb))
            heapq.heappush(q, (ladders[one_d(nb)], nb))

    # print(q)
    # print(curr)
    printvisited()
    visited[one_d(curr)] = True

print(ladders[one_d((rows-1, cols-1))])
