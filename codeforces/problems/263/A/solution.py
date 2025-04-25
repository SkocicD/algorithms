for r in range(5):
    l = list(map(int, input().split()))
    if 1 in l:
        print(abs(2-r)+abs(2-l.index(1)))
