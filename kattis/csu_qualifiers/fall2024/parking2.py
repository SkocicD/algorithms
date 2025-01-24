t = int(input())

for _ in range(t):
    input()
    ds = [int(x) for x in input().split()]
    print(2*(max(ds) - min(ds)))
