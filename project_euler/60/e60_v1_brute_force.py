import math
import time

class PrimeGenerator:
    def __init__(self):
        self.currentNum = 1

    def divides(k, n):
        return n % k == 0

    def isEven(n):
        return PrimeGenerator.divides(2, n)

    def isPrime(number):
        if number == 2:
            return True
        elif PrimeGenerator.isEven(number):
            return False
        else:
            n = 3
            isPrime = True
            while isPrime and n <= math.sqrt(number):
                if PrimeGenerator.divides(n, number):
                    isPrime = False
                else:
                    n += 2
            return isPrime

    def currentNumIsPrime(self):
        return PrimeGenerator.isPrime(self.currentNum)

    def getNextPrime(self):
        self.currentNum += 1
        while not self.currentNumIsPrime():
            self.currentNum += 1
        return self.currentNum

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


def propertyTrue(candidate):
    isPrime = True
    i = 0
    j = 1
    done = False
    maxIdx = len(candidate)-1
    while not done and isPrime:
        if i == maxIdx:
            done = True
        else:
            a = candidate[i]
            b = candidate[j]
            if PrimeGenerator.isPrime(int(str(a) + str(b))) and PrimeGenerator.isPrime(int(str(b) + str(a))):
                j += 1
                if j > maxIdx:
                    i += 1
                    j = i+1
            else:
                isPrime = False
        
    return isPrime

def displaySolution(candidate):
    print(candidate)
    print(sum(candidate))

def createCandidate(indices, primeList):
    candidate = []
    candidate.append(primeList[-1])
    for i in indices:
        candidate.append(primeList[i])
    return candidate


def searchSolution():
    startTime = time.time()
    print('Search solution')
    cPrimesNum = 5
    primeGenerator = PrimeGenerator()
    primeList = []
    done = False
    while not done:
        p = primeGenerator.getNextPrime()
        print(p)
        primeList.append(p)
        done = (p == 661)
#    for i in range(cPrimesNum - 1):
#        primeList.append(primeGenerator.getNextPrime())

    found = False
    while not found:
        indicesGenerator = IndicesGenerator(cPrimesNum - 1, len(primeList))
        primeList.append(primeGenerator.getNextPrime())
        currentTime = time.time()
        print(primeList[-1], end='')
        print(', time = ', end = '')
        print(round(currentTime - startTime))
        finishedTask = False
        while not found and not finishedTask:
            if indicesGenerator.createNext():
                indices = indicesGenerator.get()
                candidate = createCandidate(indices, primeList)
                #print(candidate)
                if propertyTrue(candidate):
                    found = True
                    displaySolution(candidate)
            else:
                finishedTask = True


def test():
    print('test')
    indicesGenerator = IndicesGenerator(3, 5)
    while indicesGenerator.createNext():
        print(indicesGenerator.get())

    print(propertyTrue([3, 7, 109, 673]))
    print(propertyTrue([7, 2, 3, 5]))

test()
searchSolution()
