n=[f'{x:4b}' for x in list(map(int,list(input())))]
[print("".join([s[i]+'_' if j!=1 else s[i]+'___' for j,s in enumerate(n)])[:-1].replace(' ','.').replace('0','.').replace('1','*').replace('_',' ')) for i in range(4)]
