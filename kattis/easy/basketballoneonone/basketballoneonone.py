a, b = (0, 0)
s = input()
for i in range(len(s))[::2]:
    ch = s[i]
    n = int(s[i+1])
    if ch == 'A':
        a += n
    else:
        b += n

print('A' if a > b else 'B')
