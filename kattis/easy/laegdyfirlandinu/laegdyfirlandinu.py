n, m = list(map(int, input().split()))
mat = []
for r in range(n):
    mat.append([])
    for ch in map(int, input().split()):
        mat[r].append(ch)
for r in range(1, n-1):
    for c in range(1, m-1):
        i = mat[r][c]
        if i < mat[r-1][c] and i < mat[r+1][c] and i < mat[r][c-1] and i < mat[r][c+1]:
            print("Jebb")
            exit()
print("Neibb")
