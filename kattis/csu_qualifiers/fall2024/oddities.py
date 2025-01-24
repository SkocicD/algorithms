n = int(input())

for _ in range(n):
    a = int(input())
    if a % 2 == 0:
        print(f'{a} is even')
    else:
        print(f'{a} is odd')
