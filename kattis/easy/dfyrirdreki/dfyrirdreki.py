a, b, c = [int(input()) for _ in range(3)]
if (d := b*b-4*a*c) > 0:
    print(2)
elif d == 0:
    print(1)
else:
    print(0)
