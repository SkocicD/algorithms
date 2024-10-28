w = input()
k = w.count('k')
b = w.count('b')
if b == 0 and k == 0:
    print('none')
elif b > k:
    print('boba')
elif b < k:
    print('kiki')
else:
    print('boki')
