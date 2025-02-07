t = int(input())
for _ in range(t):
    p = 1
    for i in range(int(input())):
        p *= (i+1)
        p %= 10
    print(p)
