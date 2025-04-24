for _ in range(int(input())):
    (input(), input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    while len(a) > 0 and len(b) > 0:
        if a[-1] < b[-1]:
            a.pop(-1)
        else:
            b.pop(-1)
    if len(a) > 0:
        print('Godzilla')
    else:
        print('MechaGodzilla')
