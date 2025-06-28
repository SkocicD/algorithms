while (t := tuple(map(int, input().split()))) != (0, 0):
    a, b = t
    if a+b == 13:
        print('Never speak again.')
    elif a == b:
        print('Undecided.')
    elif a > b:
        print('To the convention.')
    else:
        print('Left beehind.')
