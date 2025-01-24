a=[1,1,2,2,2,8]
b=[int(x) for x in input().split()]
s=''
for i in range(6):
    s+=str(a[i]-b[i]) + ' '
s=s[:-1]
print(s)
