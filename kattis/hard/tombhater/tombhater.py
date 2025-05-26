rows, cols, words = list(map(int, input().split()))
mat = [[0 for x in range(rows*cols)] for y in range(rows*cols)]
board = [input().split() for x in range(rows)]
wordtree = {}


def get(r, c):
    global board
    return board[r][c]


for _ in range(words):
    word = input()
    currdict = wordtree
    for i, let in enumerate(word):
        if let not in currdict:
            currdict[let] = {}
        currdict = currdict[let]
        if i == len(word) - 1:
            currdict['END'] = 'XXX'

queue = []
currdict = wordtree

# print(wordtree)
minnumsteps = 999999


def dfs(pos, numsteps, currdict, visited):
    global minnumsteps
    r, c = pos

    steps = [999999, 999999, 999999, 999999, 999999, 999999]
    currch = get(r, c)
    visited.add(pos)
    if currch in currdict:
        if 'END' in currdict[currch] and r == rows-1:
            minnumsteps = min(minnumsteps, numsteps)
            return numsteps
        if c != 0:
            newpos = (r, c-1)
            if newpos not in visited:
                steps[0] = dfs(newpos, numsteps+1,
                               currdict[currch], visited)
        if c != cols-1:
            newpos = (r, c+1)
            if newpos not in visited:
                steps[1] = dfs(newpos, numsteps+1,
                               currdict[currch], visited)
        if r != rows-1:
            newpos = (r+1, c)
            if newpos not in visited:
                steps[2] = dfs(newpos, numsteps+1,
                               currdict[currch], visited)

    if 'END' in currdict:
        currdict = wordtree
    if currch in currdict:
        if 'END' in currdict[currch] and r == rows-1:
            minnumsteps = min(minnumsteps, numsteps)
            return numsteps
        if c != 0:
            newpos = (r, c-1)
            if newpos not in visited:
                steps[3] = dfs(newpos, numsteps+1,
                               currdict[currch], visited)
        if c != cols-1:
            newpos = (r, c+1)
            if newpos not in visited:
                steps[4] = dfs(newpos, numsteps+1,
                               currdict[currch], visited)
        if r != rows-1:
            newpos = (r+1, c)
            if newpos not in visited:
                steps[5] = dfs(newpos, numsteps+1,
                               currdict[currch], visited)

    visited.remove(pos)
    minnumsteps = min(minnumsteps, min(steps))
    return minnumsteps


# best = 999999
for c in range(cols):
    dfs((0, c), 1, wordtree, set())

print(minnumsteps if minnumsteps < 999999 else 'impossible')
