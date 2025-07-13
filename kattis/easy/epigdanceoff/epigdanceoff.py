d = [input() for _ in '_'*int(input().split()[0])]
print(sum('$' not in s for s in zip(*d))+1)
