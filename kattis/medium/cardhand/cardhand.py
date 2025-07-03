from itertools import permutations
import bisect


# some combination of shdc, sorting the list in that order of suits
# capital letters will mean reverse order
def encode(pattern: str, cards):
    values = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5,
              '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
    numbers = []
    for card in cards:
        i = pattern.lower().index(card[1])
        num = 0
        num += 13 * i
        if pattern[i].isupper():
            num += 12-values[card[0]]
        else:
            num += values[card[0]]
        numbers.append(num)
    return numbers


def min_moves_to_sort(arr):
    lis = []
    for x in arr:
        idx = bisect.bisect_left(lis, x)
        if idx == len(lis):
            lis.append(x)
        else:
            lis[idx] = x
    return len(arr) - len(lis)


# iterate over every possible pattern
letters = ['s', 'd', 'h', 'c']
patterns = []

# Generate all case variants with unique base letters
for p in permutations(letters, 4):
    # For each permutation, apply all case combinations (2^4)
    for mask in range(16):  # 0000 to 1111
        pattern = []
        for i, ch in enumerate(p):
            if (mask >> i) & 1:
                pattern.append(ch.upper())
            else:
                pattern.append(ch.lower())
        patterns.append(''.join(pattern))

input()
cards = input().split()
print(min([min_moves_to_sort(encode(pattern, cards)) for pattern in patterns]))
