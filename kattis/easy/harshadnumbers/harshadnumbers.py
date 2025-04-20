def isH(n):
    return n % sum(map(int, [i for i in str(n)])) == 0


n = int(input())

while not isH(n):
    n += 1
print(n)
