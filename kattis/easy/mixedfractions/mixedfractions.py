while (t := tuple(map(int, input().split()))) != (0, 0):
    a, b = t
    s = ''
    print(f'{a//b} {a-b*(a//b)} / {b}')
