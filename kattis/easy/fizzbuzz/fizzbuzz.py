x, y, n = list(map(int, input().split()))
for i in range(1, n+1):
    s = ''
    if i % x == 0:
        s += 'Fizz'
    if i % y == 0:
        s += 'Buzz'
    print(i if s == '' else s)
