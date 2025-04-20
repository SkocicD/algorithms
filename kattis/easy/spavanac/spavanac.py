h, m = list(map(int, input().split()))
a = (60*h+m-45) % (24*60)
print(a//60, a % 60)
