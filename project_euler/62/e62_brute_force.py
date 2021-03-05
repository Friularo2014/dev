from itertools import permutations

def getPermutations(c):
    res = []
    s = str(c)
    n = pow(10, len(s)-1)
    for e in set([''.join(p) for p in permutations(s)]):
        k = int(e)
        if k >= n:
            res.append(int(e))
    #print('number of permutations of c = ' + str(c) + ' = ' + str(len(res)))
    return res

def isCube(n):
    m0 = n**(1/3)
    m = round(m0)
    #print('n = ' + str(n) + ', m0 = ' + str(m0) + ', m = ' + str(m) + ', pow(m, 3) = ' + str(pow(m, 3)))
    res = (n == pow(m, 3))
    #if res: print('isCube True ' + str(n))
    return res

desiredNumOfPermutations = 5
done = False
n = 1
while not done:
    n += 1
    c = pow(n, 3)
    print(n)
    #print(c)
    cNum = 0
    for p in getPermutations(c):
        if isCube(p):
            cNum += 1
    if cNum == desiredNumOfPermutations:
        print('Solution: ' + str(c))
        done = True


#print(isCube(41063625))
#print(isCube(56623104))
#print(isCube(66430125))
#
#print(isCube(56206413))
#print(isCube(1365624))
#print(isCube(31650642))
