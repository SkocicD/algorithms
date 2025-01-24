from functools import cache

n, m, k = [int(x) for x in input().split()]
passengers = [0] + [int(x) for x in input().split()]
carts = []
for _ in range(m):
    left, right = [int(x) for x in input().split()]
    carts.append({'l':left, 'r':right})

# sort(carts)
@cache
def count_in_span(left, right):
    total = 0
    for i in range(left, right + 1):
        total += passengers[i]
    return total

@cache
def minimum_r(left):
    global passengers
    total = passengers[left]
    while total < k:
        left += 1
        total += passengers[left]
    return left

@cache
def maximum_l(right):
    global passengers
    total = passengers[right]
    while total < k:
        right -= 1
        total += passengers[right]
    return right

def get_allowed_ranges(left, right):
    global passengers
    global k
    max_l = maximum_l(right)
    min_r = minimum_r(left)
    currpassengers = count_in_span(left, min_r)
    max_r = right
    right = min_r
    
    allowed_ranges = [(left, min_r)]

    while left <= max_l:
        # always step one to the left
        currpassengers -= passengers[left]
        left += 1

        while currpassengers < k and right <= max_r:
            right += 1
            currpassengers += passengers[right-1]

        allowed_ranges.append((left,right))
    return allowed_ranges

def get_respective_r(allowed_ranges, l):
    lower = 0
    upper = len(allowed_ranges) - 1
    while upper > lower:
        middle = lower + (upper - lower)//2
        if l < allowed_ranges[middle][0]:
            upper = middle - 1

        elif l == allowed_ranges[middle][0]:
            return allowed_ranges[middle][1]
        else:
            lower = middle + 1
    return allowed_ranges[lower][1]


def get_cart_configuration_count(carts, not_none, rightmost_l, leftmost_r):
    # print(carts)
    global k
    total = 0
    removed = []
    allowed_ranges = get_allowed_ranges(rightmost_l, leftmost_r)
    not_none_2 = []
    while len(not_none) > 0:
        i = not_none.pop()
        cart = carts[i]
        left = max(rightmost_l, cart['l'])

        # if the left is too large then remove it from the list
        if left > allowed_ranges[-1][0]:
            carts[i] = None
            removed.append((i,cart))
            continue

        # if the required right bound is bigger than the actual, remove it
        required_r = get_respective_r(allowed_ranges, left)
        right = min(leftmost_r, cart['r'])
        if right < required_r:
            carts[i] = None
            removed.append((i,cart))
            continue

        not_none_2.append(i) 

    while len(not_none_2) > 0:
        i = not_none_2.pop()
        cart = carts[i]
        removed.append((i, cart))
        carts[i] = None
        total += get_cart_configuration_count(carts, not_none_2, max(rightmost_l, cart['l']), min(leftmost_r, cart['r']))
                                    
    for i, cart in removed:
        carts[i] = cart
        not_none.append(i)
    return 1 + total
    
total = 0
not_none = []
for i, cart in enumerate(carts):
    if count_in_span(cart['l'], cart['r']) < k:
        carts[i] = None
    else:
        not_none.append(i)

while len(not_none) > 0:
    i = not_none.pop()
    cart = carts[i]
    carts[i] = None
    total += get_cart_configuration_count(carts, not_none, cart['l'], cart['r'])

print(total)

