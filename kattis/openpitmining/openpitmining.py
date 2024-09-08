class Node ():
    def __init__(self, value, cost):
        self.net = value - cost
        self.tempcovers = []
        self.covers = []
        self.coveredby  = []
        self.valueToPoint = None

    def get_removal_value(self):
        sum = self.net
        for node in self.coveredby:
            sum += node.net
        return sum

value = 0

# search down the graph until we find a node with a positive removal value
def search(node):
    global value
    valueifremoved = node.get_removal_value()
    if valueifremoved > 0:
        value += valueifremoved
        # remove everything leading up to this node
        removeAllCovers(node)
        return True
    for child in node.covers:
        if search(child):
            return True
    return False

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

# fill in all nodes with their values and the node numbers they point to
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
# while there wasnt an increase in value from one loop to the next
while temp < value:
    temp = value
    for node in nodes:
        # if the rock isnt covered
        if len(node.coveredby) == 0:
            if search(node):
                break

print(value)

