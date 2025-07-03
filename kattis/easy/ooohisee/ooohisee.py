def ngbrs(b, r, c):
    global rows
    global cols
    if r == 0 or c == 0 or r == rows-1 or c == cols-1:
        return False
    return [b[r-1][c-1], b[r-1][c], b[r-1][c+1], b[r][c-1], b[r][c+1], b[r+1][c-1], b[r+1][c], b[r+1][c+1]]


rows, cols = list(map(int, input().split()))
board = [list(input()) for _ in range(rows)]
locs = []
for r in range(rows):
    for c in range(cols):
        if board[r][c] == '0':
            nb = ngbrs(board, r, c)
            if nb:
                if '0' not in nb:
                    locs.append((r+1, c+1))
match len(locs):
    case 0:
        print('Oh no!')
    case 1:
        print(*locs[0])
    case _:
        print(f'Oh no! {len(locs)} locations')
