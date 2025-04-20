for _ in range(int(input())):
    a, b = input().split()
    b = int(b)
    b = b*(b+1)//2+b
    print(a, b)
