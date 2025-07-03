t, n = list(map(float, input().split()))
n = int(n)
veg = list(map(int, input().split()))
pieces = [1] * n

cuts = 0
while True:
    # find veg with biggest pieces that has already had the most cuts
    minperpiece = 9999999999
    maxperpiece = 0
    maxindex = 0
    for i in range(n):
        if veg[i] / pieces[i] < minperpiece:
            minperpiece = veg[i] / pieces[i]
        if veg[i] / pieces[i] > maxperpiece:
            maxperpiece = veg[i] / pieces[i]
            maxcuts = pieces[i]
            maxindex = i

    # check if our pieces are the right size
    if minperpiece/maxperpiece > t:
        print(cuts)
        exit()

    # now we cut the piece at maxindex
    pieces[maxindex] += 1
    cuts += 1
