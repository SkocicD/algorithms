try:
    n = input().index('tree')
except:
    n = -1
print(n if n > -1 else 'no trees here')
