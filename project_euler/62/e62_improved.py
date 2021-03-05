class Node:
    def __init__(self):
        self.numbers = []
        self.children = {}

def createTreePath(node, n, cubeStrArr):
    if len(cubeStrArr) == 0:
        node.numbers.append(n)
        return node
    else:
        c = cubeStrArr.pop()
        if c not in node.children.keys():
            node.children[c] = Node()
        return createTreePath(node.children[c], n, cubeStrArr)

def addToTree(root, n):
    cube = pow(n, 3)
    cubeStrArr = sorted(str(cube), reverse = True)
    return createTreePath(root, n, cubeStrArr)

def printSpaces(level, s, end = '\n'):
    for i in range(level):
        print(' ', end='')
    print(s, end=end)

def printTree(node, level=0):
    print(node.numbers)
    for c in node.children.keys():
        printSpaces(level+1, str(c) + ': ', '')
        printTree(node.children[c], level+1)


N = 5
root = Node()
found = False
n = 0
while not found:
    n += 1
    node = addToTree(root, n)
    if len(node.numbers) == N:
        found = True
        print(node.numbers)
        for i in node.numbers:
            print(pow(i, 3))
