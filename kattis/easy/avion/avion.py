ans = []
for i in range(5):
    if 'FBI' in input():
        ans.append(i+1)
if len(ans) > 0:
    print(*ans)
else:
    print('HE GOT AWAY!')
