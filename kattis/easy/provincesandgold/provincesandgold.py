g, s, c = list(map(int, input().split()))
total = 3*g+2*s+c
s = ''
if total >= 8:
    s += 'Province'
elif total >= 5:
    s += 'Duchy'
elif total >= 2:
    s += 'Estate'
if s != '':
    s += ' or '
if total >= 6:
    s += 'Gold'
elif total >= 3:
    s += 'Silver'
else:
    s += 'Copper'
print(s)
