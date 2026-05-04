def h(x):
    if x == 1:
        return 1
    if x % 2:
        return x + h(3*x+1)
    return x + h(x//2)
print(h(int(input())))
