n,k = [int(x) for x in input().split()]
bs = [int(x) for x in input().split()]
i = bs.index(k)

if i==0:
    print('fyrst')
elif i==1:
    print('naestfyrst')
else:
    print(f'{i+1} fyrst')
