input()
s1 = sum(map(int, input().split()))
s2 = sum(map(int, input().split()))
if s1 == s2:
    print('Oh no')
else:
    print('Button 1' if s1 > s2 else 'Button 2')
