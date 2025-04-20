s = input().lower()
print(sum(1 for i in s if i in "aeiou"),
      sum(1 for i in s if i in "yaeiou"))
