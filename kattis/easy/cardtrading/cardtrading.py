from collections import Counter
from bisect import insort
n, t, k = list(map(int, input().split()))

hand = Counter(map(int, input().split()))


def insert_in_order(q, card):
    low = 0
    up = len(q)-1

    while low < up:
        mid = (up + low)//2
        if q[mid][1] < card[1]:
            low = mid + 1
        else:
            up = mid
    q.insert(low, card)


prices = []
for i in range(t):
    a, b = tuple(map(int, input().split()))
    inhand = hand[i+1]
    prices.append(((2-inhand) * a, inhand * b))

q = []
total = 0
for card in prices:
    # take a card if there arent k combos yet
    if len(q) < k:
        total -= card[0]
        insort(q, card, key=lambda x: x[1])
        # insert_in_order(q, card)
    else:
        if q[-1][1] > card[0]:
            total += sum(q.pop())
            total -= card[0]
            insort(q, card, key=lambda x: x[1])
            # insort(q, card[1])
            # insert_in_order(q, card)
        else:
            total += card[1]
print(total)
# print(q)
