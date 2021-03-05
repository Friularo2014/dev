k = 1
done = False
count = 0
for n in range(1, 10):
    done = False
    k = 1
    while not done:
        m = pow(n, k)
        numOfDigits = len(str(m))
        if numOfDigits == k:
            count += 1
            print(str(count) + ': numOfDigits = ' + str(numOfDigits) + ', ' + str(n) + ' ^ ' + str(k) + ' = ' + str(m))
            k += 1
        elif numOfDigits < k:
            done = True
        else:
            k += 1
