n, m = list(map(int, input().split()))

# winner[r][c] is true if the first person to take a turn on a board of
# r+1 rows and c+1 columns will win the game, false if they will lose.
winner = [[False]]  # Start with the base case of a 1x1 being a loss.

for r in range(n):
    # add a row to the winner table
    if r == len(winner):
        winner.append([])

    for c in range(m):
        # this just skips over if r and c are 0 because the base case is already filled in
        if c < len(winner[r]):
            continue

        # try each cut along the row axis
        # ixc and (r-i-1)xc are the dimensions of the two pieces
        added = False
        for i in range((r+1)//2):
            if not winner[i][c] and not winner[r-i-1][c]:
                winner[r].append(True)
                break

        # if we added a winner for these dimensions, we can move on
        if c < len(winner[r]):
            continue

        # try to cut along column axis
        # rxi and rx(c-i-1) are the dimensions of the two pieces
        for i in range((c+1)//2):
            if not winner[r][i] and not winner[r][c-i-1]:
                winner[r].append(True)
                break

        # if we added a winner for these dimensions, we can move on
        if c < len(winner[r]):
            continue

        # if we reach this point, there is no way for the starting player
        # to win when these dimensions start, so set false.
        winner[r].append(False)

print('A' if winner[n-1][m-1] else 'B')
