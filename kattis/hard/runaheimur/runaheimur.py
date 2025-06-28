class Tile:
    def __init__(self, num):
        global rows
        global cols
        self.num = num
        self.goalrow = num // rows
        self.goalcol = num % cols
        self.row = -1
        self.col = -1

    def setpos(self, r, c):
        self.row = r
        self.col = c

    def __str__(self):
        return f'{self.num}: ({self.row}, {self.col})'

    def isInPlace(self):
        return self.goalrow == self.row and self.goalcol == self.col

    def peekAbove(self):
        global board
        if self.row == 0:
            return None
        else:
            return board[self.row-1][self.col]

    def peekLeft(self):
        global board
        if self.col == 0:
            return None
        else:
            return board[self.row][self.col-1]

    def peekRight(self):
        global board
        if self.col == len(board[0])-1:
            return None
        else:
            return board[self.row][self.col+1]

    def peekBelow(self):
        global board
        if self.col == len(board)-1:
            return None
        else:
            return board[self.row+1][self.col]

    def neighbors(self):
        return [self.peekBelow(), self.peekRight(),
                self.peekLeft(), self.peekAbove()]


def move(dir):
    if dir == 'l':
        tile = board[hole.row][hole.col+1]
    if dir == 'r':
        tile = board[hole.row][hole.col-1]
    if dir == 'u':
        tile = board[hole.row+1][hole.col]
    if dir == 'd':
        tile = board[hole.row-1][hole.col]
    tilepos = (tile.row, tile.col)
    holepos = (hole.row, hole.col)
    tile.row = holepos[0]
    tile.col = holepos[1]
    hole.row = tilepos[0]
    hole.col = tilepos[1]
    board[tile.row][tile.col] = tile
    board[hole.row][hole.col] = None


def printBoard():
    for r in range(rows):
        s = ''
        for c in range(cols):
            if board[r][c] is not None:
                s += f'{board[r][c].num} '
            else:
                s += '. '
        print(s)


def movehole(dir):
    if dir == 'l':
        move('r')
    if dir == 'r':
        move('l')
    if dir == 'u':
        move('d')
    if dir == 'd':
        move('u')


def move_hole_to(r, c):
    # find shortest path to move the hole to r, c
    global currtile
    global completed_nums
    global hole

    q = []
    parents = {}
    curr = hole
    visited = set()
    while curr.row != r and curr.col != c:
        for nbr in curr.neighbors():
            print(nbr.row, nbr.col)
            if nbr is not None and nbr.num not in completed_nums and nbr != currtile and nbr.num not in visited:
                dist = abs(nbr.row - r) + abs(nbr.col - c) + \
                    abs(nbr.row - hole.row) + abs(nbr.col - hole.col)
                i = 0
                while i < len(q):
                    if q[i][0] > dist:
                        q.insert(i, nbr)
                        break
                    i += 1
                if len(q) == 0:
                    q.append((dist, nbr))
                parents[nbr.num] = curr
            visited.add(curr.num)
            curr = q.pop(0)[1]
    path = []
    while curr.num not in parents:
        path.insert(0, curr)
        curr = parents[curr.num]
    return path


# def move
rows, cols = list(map(int, input().split()))

board = [[None for col in range(cols)] for row in range(rows)]
tiles = []

for i in range(rows*cols-1):
    tile = Tile(i)
    tiles.append(tile)

hole = Tile(rows*cols-1)

for r in range(rows):
    currrow = list(map(int, input().split()))
    for c in range(cols):
        # ignore the tile that becomes the hole
        if currrow[c]-1 != rows*cols-1:
            board[r][c] = tiles[currrow[c]-1]
            board[r][c].setpos(r, c)
        else:
            board[r][c] = hole
            board[r][c].setpos(r, c)

print()
printBoard()
completed_nums = set()
currtile = tiles[0]
print(move_hole_to(0, 1))

exit()

for r in range(rows):
    for c in range(cols):
        currtile = tiles[r*cols + c]
        # move tile directly to its position
        if cols-c < 2:
            # do readjustment
            pass
