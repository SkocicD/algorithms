cs=set()
for i in range(int(input())):
    a,c=[x.split() for x in input().split('-> ')]
    for ai in a:
        if ai not in cs:
            print(i+1)
            exit()
    cs.add(c[0])
print('correct')
