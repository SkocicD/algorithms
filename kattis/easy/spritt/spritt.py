n, x = [int(x) for x in input().split()]

for _ in range(n):
    x-=int(input())

print('Jebb' if x >= 0 else 'Neibb')
