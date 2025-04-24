l = ['keys', 'phone', 'wallet']
for _ in range(int(input())):
    if (s := input()) in l:
        l.remove(s)
for s in l:
    print(s)
if len(l) == 0:
    print('ready')
