n = int(input())
words = []
def insert(words, word):
    if len(words) == 0:
        words.append(word)
        return
    lower = 0
    upper = len(words) - 1
    while lower < upper:
        middle = lower + (upper - lower) // 2
        if word < words[middle]:
            upper = middle - 1
        elif word == words[middle]:
            words.insert(middle, word)
            return
        else:
            lower = middle + 1

    if words[upper] > word:
        words.insert(upper, word)
    else:
        words.insert(upper+1, word)

def find(words, word):
    if len(words) == 0:
        return 0
    lower = 0
    upper = len(words) - 1
    while lower < upper:
        middle = lower + (upper - lower) // 2
        if word < words[middle]:


for _ in range(n):
    word = input()
    insert(words, input())
    count = 0
    print(words)
    # for word in words[:-1]:
        # if word[0:len(words[-1])] == words[-1]:
            # count += 1
        # print(words)
