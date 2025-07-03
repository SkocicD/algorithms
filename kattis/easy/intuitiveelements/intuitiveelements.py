for _ in range(int(input())):
    a = set(input())
    b = set(input())
    print('YES' if b == a.intersection(b) else 'NO')
