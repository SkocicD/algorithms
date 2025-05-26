class index:
    def __init__(self, ind):
        self.ind = ind
        self.sum = 0
        self.queries = 0

    def doqueries(self, queries):
        for query in queries[self.queries:]:
            a, b, c = query
            if self.ind % b == a % b:
                self.sum += c
        self.queries = len(queries)


N, Q = list(map(int, input().split()))

array = [index(i) for i in range(N+1)]
queries = []
for _ in range(Q):
    line = list(map(int, input().split()))
    if line[0] == 1:
        queries.append(line[1:])
    else:
        i = line[1]
        array[i].doqueries(queries)
        print(array[i].sum)
