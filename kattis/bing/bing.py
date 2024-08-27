n = int(input())
words = []

def find(words, word):
    lower = 0
    upper = len(words) - 1
    while lower < upper:
        middle = lower + (upper - lower) // 2
        if word < words[middle]:
            upper = middle - 1
        elif word == words[middle]:
            upper = middle
        else:
            lower = middle + 1
    if upper < 0:
        return 0
    if words[upper] >= word:
        return upper
    else:
        return upper + 1

for _ in range(n):
    word = input()
    if len(words) > 0:
        start = find(words, word)
        end = find(words, word + chr(ord('z')+1))
    else:
        start = 0
        end = 0
    print(end - start)
    words.insert(start, word)
