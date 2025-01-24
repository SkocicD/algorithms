ls = input()
ws = input().split()

d1 = {}
d2 = {}
class combo:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def get_l(self, l):
        if self.l == l:
            return self.w
        else:
            return False
    
    def get_w(self, w):
        if self.w == w:
            return self.l
        else:
            return False

combos = []

if len(ls) != len(ws):
    print(False)
    exit()

for l, w in zip(ls, ws):

    for c in combos:
        if (c.l == l and c.w != w) or (c.w == w and c.l != l):
            print(False)
            exit()
    else:
        combos.append(combo(l, w))

print("True")
