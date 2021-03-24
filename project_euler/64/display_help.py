prefix = 'return ['
myList = ['d', 'e', 'b']
suffix = " + ']'"
#myList.append('x')
#myList.append('y')
#for i in range(ord('a'), ord('e')+1):
#    myList.append(chr(i))
print("print(", end='')
first = True
for a in myList:
    if not first: print(' + ', end='')
    print("'", end='')
    if first: print(prefix, end='')
    if not first: print(', ', end='')
    print(a + " = ' + str(" + a + ')', end='')
    first = False
print(suffix + ')')
