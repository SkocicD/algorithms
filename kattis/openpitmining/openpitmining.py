class Node ():
    def __init__(self, value, cost):
        self.net = value - cost
        self.tempcovers = []
        self.covers = []
        self.coveredby  = []
        self.valueToPoint = None

value = 0

def removeAllCovers(node):
    global nodes
    while len(node.coveredby) > 0:
        nodes.remove(node.coveredby.pop())
    nodes.remove(node)
    for n in nodes:
        i = 0
        while i < len (n.coveredby):
            parent = n.coveredby[i]
            if parent not in nodes:
                n.coveredby.pop(i)
            else:
                i += 1

def fillcovers(node):
    for child in node.covers:
        for parent in node.coveredby:
            if parent not in child.coveredby:
                child.coveredby.append(parent)
        fillcovers(child)

n = int(input())

nodes = []

for _ in range(n):
    line = [int(x) for x in input().split()]
    nodes.append(Node(line[0],line[1]))
    for i in range(line[2]):
        nodes[-1].tempcovers.append(line[3 + i])
# tell each node who it covers (by reference) and who covers it
for node in nodes:
    while len(node.tempcovers) > 0:
        nodenum = node.tempcovers.pop()
        node.covers.append(nodes[nodenum - 1])
        nodes[nodenum - 1].coveredby.append(node)

for node in nodes:
    if len(node.coveredby) == 0:
        fillcovers(node)

temp = -1
while temp < value:
    temp = value
    for node in nodes:
        node.valueToPoint = node.net
        for parent in node.coveredby:
            node.valueToPoint += parent.net
        if node.valueToPoint > 0:
            removeAllCovers(node)
            value += node.valueToPoint
            break

print(value)

