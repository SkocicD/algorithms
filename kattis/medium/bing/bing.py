letters = {}
for _ in range(int(input())):
    currdict = letters
    for ch in input():
        if ch not in currdict:
            currdict[ch] = {}
            currdict[ch]['count'] = -1
        currdict[ch]['count'] += 1
        currdict = currdict[ch]
    print(currdict['count'])
