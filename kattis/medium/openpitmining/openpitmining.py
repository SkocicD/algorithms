class Node ():
    def __init__(self, value, cost):
        self.net = value - cost
        self.tempcovers = []
        self.covers = []
        self.coveredby  = set()
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
        return node
    for child in node.covers:
        removedNode = search(child)
        if removedNode is not None:
            return removedNode

def removeAllCovers(node):
    global nodes
    for n in node.coveredby:
        nodes.remove(n)
    nodes.remove(node)
    for n in nodes:
        for parent in n.coveredby:
            toremove = set()
            if parent not in nodes:
                toremove.add(parent)
        for parent in toremove:
            n.coveredby.remove(parent)

def fillcovers(node):
    for child in node.covers:
        for parent in node.coveredby:
            child.coveredby.add(parent)
        fillcovers(child)

n = int(input())

nodes = set()

# fill in all nodes with their values and the node numbers they point to
for _ in range(n):
    line = [int(x) for x in input().split()]
    newnode = Node(line[0], line[1])
    nodes.add(newnode)
    for i in range(line[2]):
        newnode.tempcovers.append(line[3 + i])

# tell each node who it covers (by reference) and who covers it
for node in nodes:
    while len(node.tempcovers) > 0:
        nodenum = node.tempcovers.pop()
        node.covers.append(nodes[nodenum - 1])
        nodes[nodenum - 1].coveredby.add(node)

for node in nodes:
    if len(node.coveredby) == 0:
        fillcovers(node)

temp = -1
# while there wasnt an increase in value from one loop to the next
while temp < value:
    temp = value
    removedNode = None
    for node in nodes:
        # if the rock isnt covered
        if len(node.coveredby) == 0:
            removedNode = search(node)
            if removedNode is not None:
                break
    if removedNode is not None:
        removeAllCovers(removedNode)

print(value)

