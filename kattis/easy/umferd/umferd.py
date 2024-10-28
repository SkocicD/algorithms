m = int(input())
n = int(input())
count = 0
for _ in range(n):
    count += input().count('#')
print(1 - count / (m*n))
