n = 7
for _ in range(int(input())):
    if (s := input()) == 'Skru op!' and n < 10:
        n += 1
    elif s == 'Skru ned!' and n > 0:
        n -= 1
print(n)
