s = []
for ch in input():
    if ch == '<' and len(s) > 0:
        s.pop(-1)
    else:
        s.append(ch)
print(''.join(s))
