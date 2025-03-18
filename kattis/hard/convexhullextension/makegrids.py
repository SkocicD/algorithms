from itertools import pairwise
from fractions import Fraction

n = int(input())
denom = n
s = ''
sums=[]
for i in range(n-1,1,-1):
    slope = Fraction(i,denom)
    # check if coprime
    sum=0
    rowsums=[]

    if slope.denominator == n:
        for j in range(2,n):
            result=slope*j
            intresult=result.numerator//result.denominator
            sum+=intresult
            rowsums.append(sum)
            s+=str(intresult) + ' '
        s+='| '+str(sum)+' // '+str(sum/intresult)+'\n'
        sums.append(rowsums)
print(s)
s=''
[print(row) for row in sums]
