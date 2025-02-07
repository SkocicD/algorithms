r,c,zr,zc = list(map(int, input().split()))
columns = ''.join([zc*char for char in ''.join([input() for _ in range(r)])])
print(''.join([(columns[i:i+c*zc]+'\n')*zr for i in range(0,len(columns),c*zc)])[:-1])
