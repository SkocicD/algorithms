import sys
low1 = 1
up1 = 500
low2 = 1
up2 = 500

def mid(low, up):
    return low + int((up - low)/2)

while low1 != up1 or low2 != up2:
    mid1 = mid(low1, up1)
    mid2 = mid(low2, up2)
    if up1 > up2:
        mid2 += 1
        glow = mid2
        gup = mid1
        print(f'ASK {glow} {gup}')
        r1,r2 = input().split()
        sys.stdout.flush()

        if r1 == 'yes':
            up1 = mid1 
        else:
            low1 = mid1 + 1

        if r2 == 'yes':
            low2 = mid2 
        else:
            up2 = mid2 - 1
    elif up1 < up2:
        mid1 += 1
        glow = mid1
        gup = mid2
        print(f'ASK {glow} {gup}')
        r1,r2 = input().split()
        sys.stdout.flush()

        if r1 == 'yes':
            low1 = mid1
        else:
            up1 = mid1 - 1

        if r2 == 'yes':
            up2 = mid2 
        else:
            low2 = mid2 + 1
    else:
        glow = low1
        gup = mid2
        print(f'ASK {glow} {gup}')
        r1,r2 = input().split()
        sys.stdout.flush()

        if r1 == 'yes':
            up1 = mid1 
        else:
            low1 = mid1 + 1

        if r2 == 'yes':
            up2 = mid2 
        else:
            low2 = mid2 + 1

print(f'GUESS {low1} {low2}')
'''
    print(f'Ranges 1:{(low1,up1)} 2:{(low2, up2)}')
    print(f'ASK {glow} {gup}')
    r1,r2 = input().split()
    sys.stdout.flush()

    if r1 == 'yes':
        up1 = mid1 
    else:
        low1 = mid1

    if r2 == 'yes':
        up2 = mid2 
    else:
        low2 = mid2
'''
