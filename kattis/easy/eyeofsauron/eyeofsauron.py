print('correct' if (s := input())[:len(s)//2-1]
      == s[len(s)//2+1:] else 'fix')
