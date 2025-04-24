a, b, c, d, e = list(map(int, input().split()))
g = int(input())
if g < e:
    print('F')
elif g < d:
    print('E')
elif g < c:
    print('D')
elif g < b:
    print('C')
elif g < a:
    print('B')
else:
    print('A')
