prevch = None
s = ''
for ch in input():
    if prevch != ch:
        s += ch
        prevch = ch
print(s)
