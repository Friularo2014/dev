import math

N = 5

class IndicesGenerator:
    def __init__(self, subsetLen, setLen):
        self.subsetLen = subsetLen
        self.setLen = setLen
        self.v = []

    def increase(self, idx):
        if idx < 0:
            return False
        self.v[idx] += 1
        if self.v[idx] > self.setLen - (self.subsetLen - idx):
            if self.increase(idx-1):
                self.v[idx] = self.v[idx-1] + 1
                return True
            else:
                return False
        else:
            return True

    def createNext(self):
        if not self.v:
            for i in range(self.subsetLen):
                self.v.append(i)
            return True
        else:
            return self.increase(len(self.v)-1)

    def get(self):
        return self.v


class Vertex:
    def __init__(self, p):
        self.prime = p
        self.neighbours = []

class PrimeFactory:
    def __init__(self):
        self.currentNum = 1

    def divides(k, n):
        return n % k == 0

    def isEven(n):
        return PrimeFactory.divides(2, n)

    def isPrime(number):
        if number == 2:
            return True
        elif PrimeFactory.isEven(number):
            return False
        else:
            n = 3
            isPrime = True
            while isPrime and n <= math.sqrt(number):
                if PrimeFactory.divides(n, number):
                    isPrime = False
                else:
                    n += 2
            return isPrime

    def currentNumIsPrime(self):
        return PrimeFactory.isPrime(self.currentNum)

    def getNextPrime(self):
        self.currentNum += 1
        while not self.currentNumIsPrime():
            self.currentNum += 1
        return self.currentNum


def createEdge(graph, idx1, idx2):
    graph[idx1].neighbours.append(idx2)
    graph[idx2].neighbours.append(idx1)


def printSolution(graph, vIdx, n):
    s = []
    for i in n:
        s.append(graph[i].prime)
    s.append(graph[vIdx].prime)
    print(s)
    print(sum(s))


def edgeExists(graph, idx0, idx1):
    res = idx0 in graph[idx1].neighbours and \
          idx1 in graph[idx0].neighbours

    return res

def areAllNeighbours(graph, c):
    res = True
    ig = IndicesGenerator(2, len(c))
    while res and ig.createNext():
        idx = ig.get()
        idx0 = c[idx[0]] 
        idx1 = c[idx[1]] 
        res = edgeExists(graph, idx0, idx1)
    return res


def checkNeighbours(graph, vIdx):
    nLen = len(graph[vIdx].neighbours)
    if nLen < N-1:
        return False

    indicesGenerator = IndicesGenerator(N-1, nLen)
    found = False
    while not found and indicesGenerator.createNext():
        c = indicesGenerator.get()
        n = []
        for i in c:
            n.append(graph[vIdx].neighbours[i])
        if areAllNeighbours(graph, n):
            found = True
            printSolution(graph, vIdx, n)

    return found 

def tenPower(n):
    k = 10
    while k < n:
        k *= 10
    return k

def propertySatisfied(graph, vIdx1, vIdx2):
    v1 = graph[vIdx1]
    p1 = v1.prime
    m1 = tenPower(p1)

    v2 = graph[vIdx2]
    p2 = v2.prime
    m2 = tenPower(p2)

    c1 = p1*m2 + p2
    c2 = p2*m1 + p1
    res = PrimeFactory.isPrime(c1) and PrimeFactory.isPrime(c2)
    return res
    

def run():
    graph = []
    primeFactory = PrimeFactory()
    found = False
    while not found:
        newVertex = Vertex(primeFactory.getNextPrime())
        graph.append(newVertex)
        newVertexIdx = len(graph)-1
        for vIdx in range(len(graph)-2):
            if propertySatisfied(graph, newVertexIdx, vIdx):
                createEdge(graph, newVertexIdx, vIdx)

        found = checkNeighbours(graph, newVertexIdx)

run()

