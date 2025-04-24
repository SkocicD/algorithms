if (n := int(input())) % 2 == 1:
    print('still running')
else:
    total = 0
    for i in range(n//2):
        total += abs(int(input())-int(input()))
    print(total)
