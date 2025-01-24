import sys


for line in sys.stdin:
    l = [int(x) for x in line.split()] 
    total = sum(l)

    for x in l:
        if total - x == x:
            print(x)
            break
