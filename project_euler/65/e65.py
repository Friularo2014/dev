import math

scope = 100
q = []
#uq = []
#num = math.e
#for i in range(scope):
#    if i == 0:
#        q.append(math.floor(num))
#        uq.append(num)
#    else:
#        u = 1 / (uq[i-1] - q[i-1])
#        q.append(math.floor(u))
#        uq.append(u)

a = 1
q.append(2)
q.append(1)
m = 0
while len(q) < scope:
    m += 1 
    q.append(2*m)
    q.append(1)
    q.append(1)

print(q)

n = []
d = []
for i in range(scope):
    if i == 0:
        n.append(q[0])
        d.append(1)
    elif i == 1:
        n.append(n[i-1]*q[i]+d[i-1])
        d.append(d[i-1]*q[i])
    else:
        n.append(n[i-1]*q[i]+n[i-2])
        d.append(d[i-1]*q[i]+d[i-2])

print(n)
print(d)

k = n[-1]
myStr = str(k)
print(k)
s = 0
while k>0:
    s += k%10
    k = int(k/10)
print('Answer: ' + str(s))

s = 0
for c in myStr:
    s += int(c)
print('Answer: ' + str(s))

