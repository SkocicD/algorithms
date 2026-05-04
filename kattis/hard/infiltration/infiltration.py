inp = input()
letters = set(inp).remove(' ')
words = inp.split()
# go word by word and see if enforcing that it is in S works
mapping = {}
table = {2: ['be'], 3: ['our', 'rum'], 4: ['will', 'dead', 'hook', 'ship'],
         5: ['blood', 'sable'], 6: ['avenge', 'parrot'], 7: ['captain']}
for word in words:
    if len(word) in table:
        for sub in table[len(word)]:
