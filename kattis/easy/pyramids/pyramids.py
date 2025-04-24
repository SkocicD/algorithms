n = int(input())
for i in range(1, 10000, 2):
    n -= i*i
    if n < 0:
        print(i//2)
        exit()
