n,k = list(map(int,input().split()))

lets = {}

odds = 0
for _ in range(k):
    let, ct = input().split()
    ct = int(ct)
    lets[let] = ct
    if ct % 2 == 1:
        odds += 1

lets = dict(sorted(lets.items()))

if odds > n or (n-odds)%2 == 1:
    print('IMPOSSIBLE')
    exit()

mat = ['' for _ in range(n)]
for r in range(n):
    for c in range(r,n):
        # on diagonal
        if r == c:
            # if we NEED to put an odd down (or else we run out of diagonal spaces for the number of odd letters
            if odds == n-r-1:
                # find the lexiographically smallest letter with an odd count
                for let in lets:
                    if lets[let] % 2 == 1:
                        mat[r] += let
                        lets[let] -= 1
                        if lets[let] == 0:
                            del lets[let]
                        odds -= 1
                        break
            # we are free to put an odd or even down
            else:
                # get the first lexiographic letter
                firstlet = next(iter(lets))
                mat[r]+=firstlet
                lets[firstlet]-=1
                # add an odd number if we took from an even and vice versa
                if lets[firstlet]%2==1:
                    odds += 1
                else:
                    odds -= 1
                if lets[firstlet] == 0:
                    del lets[firstlet]
        else:
            for let in lets:
                if lets[let] - 2 >= 0:
                    mat[r] += let
                    lets[let] -= 2
                    if lets[let] == 0:
                        del lets[let]
                    break

input()
cols = list(map(int, input().split()))

s = ''
for row in range(len(mat)):
    for col in cols:
        if row < col-1:
            r,c = (row,col-1)
        else:
            r,c = (col-1,row)
        s += mat[r][c-r]
    s += '\n'

print(s[:-1])

