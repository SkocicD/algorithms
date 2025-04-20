spot = 1
for ch in input():
    if ch == 'A':
        if spot == 1:
            spot = 2
        elif spot == 2:
            spot = 1
    if ch == 'B':
        if spot == 2:
            spot = 3
        elif spot == 3:
            spot = 2
    if ch == 'C':
        if spot == 1:
            spot = 3
        elif spot == 3:
            spot = 1
print(spot)
