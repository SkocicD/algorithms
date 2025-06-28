lst = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1][::-1]
sum = 0
for ch in input():
    if ch != '-':
        sum += int(ch) * lst.pop()
print(int(sum % 11 == 0))
