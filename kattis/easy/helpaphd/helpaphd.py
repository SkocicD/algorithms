n = int(input())
for _ in range(n):
    s = input()
    if 'N' in s:
        print('skipped')
    else:
        print(eval(s))
