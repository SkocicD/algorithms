while (n := int(input())) != -1:
    weakv = []
    sets = []
    for r in range(n):
        sets.append(set())
        for i, e in enumerate(input().split()):
            if e == '1':
                sets[r].add(i)
    for i, s in enumerate(sets):
        for vertex in s:
            inter = s.intersection(sets[vertex])
            if len(inter) != 0:
                break
        else:
            weakv.append(i)
    print(*weakv)
