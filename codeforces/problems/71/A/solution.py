n = int(input())
for _ in range(n):
    s = input()
    print(f'{s[0]}{len(s)-2}{s[-1]}' if len(s) > 10 else s)
