class runner:
    def __init__(self):
        self.laps = 0
        self.total = 0

    def add(self, time):
        self.total += time
        self.laps += 1

l,k,s = list(map(int,input().split()))

def secs(s):
    m, s = list(map(int, s.split('.')))
    return 60*m + s

runners = {}

for _ in range(l):
    n, s =input().split()
    n = int(n)
    s = secs(s)
    if n not in runners:
        runners[n] = runner()
    runners[n].add(s)

runners = dict(sorted(runners.items(), key=lambda item: (item[1].laps, item[1].total, item[0])))

for n in runners:
    if runners[n].laps == k:
        print(n)



