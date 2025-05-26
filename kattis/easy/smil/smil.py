curr = ''
ind = 0
for i, ch in enumerate(input()):

    if ch == ':' or ch == ';':
        ind = i
        curr = ch
    elif ch == ')' and (len(curr) == 1 or len(curr) == 2):
        print(ind)
        curr = ''
    elif ch == '-' and len(curr) == 1:
        curr = curr + ch
    else:
        curr = ''
