def g(f):
    res = []
    n = 1
    done = False
    while not done:
        r = int(f(n))
        if r > 9999:
            done = True
        else:
            if r > 999:
                res.append(r)
            n += 1
    return res


def printSolution(solution):
    print(solution)
    print(sum(solution))


def checkIfAllDifferent(idxSet):
    s = set(idxSet)
    return len(s) == len(idxSet)


def checkSolution2(a, solution, idxSet):
    level = len(idxSet)
    if level == len(solution):
        return checkIfAllDifferent(idxSet)

    found = False
    for setIdx in a[solution[level]]:
        idxSet.append(setIdx)
        found = checkSolution2(a, solution, idxSet)
        if found:
            break
        else:
            idxSet.pop()
    return found

    

def checkSolution(a, solution):
    firstElem = solution[0]
    lastElem = solution[-1]
    if last2digits(lastElem) != first2digits(firstElem):
        return False

    found = False
    for setIdx in a[solution[0]]:
        idxSet = [setIdx]
        found = checkSolution2(a, solution, idxSet)
        if found: break
    return found

def first2digits(n):
    return int(str(n)[0:2])

def last2digits(n):
    return int(str(n)[-2:])

def findAllCandidates(a, number):
    candidates = []
    l2d = last2digits(number)
    for n in a.keys():
        if first2digits(n) == l2d:
            candidates.append(n)
    return candidates

def process(a, maxLevel, solution):
    if len(solution) == maxLevel:
        return checkSolution(a, solution)

    found = False
    number = solution[-1]
    candidates = findAllCandidates(a, number)
    for candidate in candidates:
        solution.append(candidate)
        found = process(a, maxLevel, solution)
        if found:
            break
        else:
            solution.pop()
    return found



l3 = lambda n: n*(n+1)/2
l4 = lambda n: n*n
l5 = lambda n: n*(3*n-1)/2
l6 = lambda n: n*(2*n-1)
l7 = lambda n: n*(5*n-3)/2
l8 = lambda n: n*(3*n-2)

s = []
s.append(g(l3))
s.append(g(l4))
s.append(g(l5))
s.append(g(l6))
s.append(g(l7))
s.append(g(l8))


a = {}
for level in range(len(s)):
    for number in s[level]:
        if number in a.keys():
            a[number].append(level)
        else:
            a[number] = [level]
for number in a.keys():
    solution = [number]
    if process(a, len(s), solution):
        printSolution(solution)
        break

