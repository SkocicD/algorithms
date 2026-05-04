miss = []
prev = 0
for _ in range(int(input())):
    for i in range(prev+1, n := int(input())):
        miss.append(i)
    prev = n

if len(miss) == 0:
    print('good job')
else:
    [print(x) for x in miss]
