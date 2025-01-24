v = int(input())
n = int(input())

for _ in range(n):
    s, k = input().split()
    k = int(k)
    print(f'{s} opin' if v <= k else f'{s} lokud')
