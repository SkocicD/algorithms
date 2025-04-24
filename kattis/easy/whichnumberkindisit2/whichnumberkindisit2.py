squares = set()
for i in range(1001):
    squares.add(i*i)
for _ in range(int(input())):
    s = ''
    n = int(input())
    if n % 2 == 1:
        s += 'O'
    if n in squares:
        s += 'S'
    if s == '':
        s = "EMPTY"
    print(s)
