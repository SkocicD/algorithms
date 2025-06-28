from math import factorial
from collections import defaultdict
from collections import Counter


def step(remain, sequence, counts, options, start):
    if remain < 0:
        return 0
    if remain == 0:
        # print(sequence)
        # print(counts)
        num = factorial(len(sequence))
        for key in counts:
            num //= factorial(counts[key])
            num *= maincounts[key[1]] ** counts[key]
        # print(num)
        return num

    total = 0
    for i, opt in options[start:]:
        sequence.append(opt)
        counts[(i, opt)] += 1
        total += step(remain-opt, sequence, counts, options, i)
        sequence.pop(-1)
        counts[(i, opt)] -= 1
    return total


m = int(input())
n = int(input())
times = []
for i in range(n):
    times.append(int(input()))
maincounts = Counter(times)
# print(maincounts)
times = list(enumerate(list(set(times))))


print(step(m, [], defaultdict(int), times, 0))
