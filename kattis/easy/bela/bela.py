n, s = input().split()
dom_m = {'A': 11, 'K': 4, 'Q': 3, 'J': 20, 'T': 10, '9': 14, '8': 0, '7': 0}
nondom_m = {'A': 11, 'K': 4, 'Q': 3, 'J': 2, 'T': 10, '9': 0, '8': 0, '7': 0}
total = 0
for _ in range(4*int(n)):
    card = input()
    if card[1] == s:
        total += dom_m[card[0]]
    else:
        total += nondom_m[card[0]]
print(total)
