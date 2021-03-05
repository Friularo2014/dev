import itertools

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



def last2digits(n):
    return int(str(n)[-2:])



def first2digits(n):
    return int(str(n)[0:2])



def checkSolution(solution):
    result = True
    for i in range(len(solution)):
        a = solution[i]
        b = solution[0] if i == len(solution)-1 else solution[i+1]
        if last2digits(a) != first2digits(b):
            result = False
            break
    return result


def process_bak(s, solution):
    level = len(solution)
    if level == len(s):
        return checkSolution(solution)

    found = False
    for n in s[level]:
        newSolution = solution.copy()
        newSolution.append(n)
        found = process(s, newSolution)
        if found:
            if level == len(s)-1:
                solution = newSolution
            break
    return found


def process(s, solution):
    level = len(solution)
    if level == len(s):
        return checkSolution(solution)

    found = False
    for n in s[level]:
        solution.append(n)
        found = process(s, solution)
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
#s.append(g(l6))
#s.append(g(l7))
#s.append(g(l8))


for p in list(itertools.permutations(s)):
    solution = []
    if process(p, solution):
        print('Final solution: ' + str(solution))
        print(sum(solution))
        break


