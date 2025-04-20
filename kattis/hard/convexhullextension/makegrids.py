from itertools import pairwise
from fractions import Fraction
from ansicolors import *


def printmat(mat):
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            print(mat[r][c],end=' ')
        print()

def printmat_color(mat):
    colormap={0:RED,1:YELLOW,2:GREEN,3:CYAN,4:PURPLE}
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            print(f'{colormap[mat[r][c]]}\u2588{ENDC}',end='')
        print()


def create_subtraction_mat(mat):
    subtraction_mat=[]
    for r in range(len(mat)):
        row=[]
        for c in range(len(mat)):
            row.append(mat[r][0] if c==0 else mat[r][c]-mat[r][c-1])
        subtraction_mat.append(row)
    return subtraction_mat

def is_symmetrical(mat):
    for r in mat:
        for a,b in list(zip(r,reversed(r)))[:len(r)//2]:
            if a!=b:
                return False
    return True


n = int(input())
denom = n
mat=[]
reduced_mat=[]
s = ''
s2 = ''
sums=[]
for i in range(n-1,1,-1):
    slope = Fraction(i,denom)
    # check if coprime
    sum=0
    rowsums=[]
    row=[]
    reduced_row=[]

    for j in range(2,n):
        result=slope*j
        intresult=result.numerator//result.denominator
        sum+=intresult
        rowsums.append(sum)
        row.append(intresult)
        if result.denominator == n: 
            reduced_row.append(intresult)

    mat.append(row)
    if slope.denominator==n:
        reduced_mat.append(reduced_row)
    sums.append(rowsums)
# [print(row) for row in sums]
printmat(mat)
print()
printmat(reduced_mat)

submat=create_subtraction_mat(mat)
reduced_submat=create_subtraction_mat(reduced_mat)

printmat(submat)
print(is_symmetrical(submat))
print()
printmat(reduced_submat)
printmat_color(reduced_submat)
print(is_symmetrical(reduced_submat))
