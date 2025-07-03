n = int(input())
y = input().split()
for i in range(n):
    try:
        if i+1 != int(y[i]):
            print("something is fishy")
            quit()
    except ValueError:
        pass
print('makes sense')
