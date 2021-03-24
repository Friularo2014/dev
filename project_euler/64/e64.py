import math

class MySqrt:

    def __init__(self, x):
        self.x = x
        self.res = []
        self.calc()

    def calc_next2(self, y, z):
        a = self.x - pow(y, 2)
        b = a / z
        c = math.floor(math.sqrt(self.x) + y)
        while c % b != 0: c -= 1
        d = c/b
        e = c-y
        #print('x = ' + str(self.x) + ', y = ' + str(y) + ', a = ' + str(a) + ', b = ' + str(b) + ', c = ' + str(c) + ', d = ' + str(d) + ', e = ' + str(e))
        #print('return [d = ' + str(d) + ', e = ' + str(e) + ', b = ' + str(b) + ']')
        return [int(d), int(e), int(b)]

    def calc(self):
        self.floor_sqrt_x = math.floor(math.sqrt(self.x))
        a = self.floor_sqrt_x
        b = a
        c = 1
        self.myList = []
        self.res.append(a)
        done = False
        while not done:
            [a, b, c] = self.calc_next2(b, c)
            if self.myList and self.myList[0][0] == a and self.myList[0][1] == b and self.myList[0][2] == c:
                done = True
            else:
                self.myList.append([a, b, c])
                self.res.append(a)


    def get(self):
        return self.res

oddPeriodCounter = 0
for i in range(10001):
    if (math.sqrt(i) != math.floor(math.sqrt(i))):
        print(str(i) + ': ' + str(MySqrt(i).get()))
        if len(MySqrt(i).get()) % 2 == 0: oddPeriodCounter += 1

print('Answer: ' + str(oddPeriodCounter))
