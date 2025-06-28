while (n := int(input())) != 0:
    i = 11
    a = sum(map(int, str(n)))
    while sum(map(int, str(n*i))) != a:
        i += 1
    print(i)
