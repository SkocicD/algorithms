s = input()+input()+input()
# print(s[::3], s[1::3], s[2::3], s[::4], s[2::2][:-1])
print('Jebb' if 'OOO' in s[0:3] or 'OOO' in s[3:6] or 'OOO' in s[6:] or 'OOO' in s[::3]
      or 'OOO' in s[1::3] or 'OOO' in s[2::3] or 'OOO' in s[::4] or 'OOO' in s[2::2][:-1] else 'Neibb')
