def d(x, y):
    if x % y == 0:
        return 1
    else:
        return 0

for a in range(1000000):
    flag = True
    for x in range(1000):
        F = (d(x, 2) <= (not(d(x, 3)))) + (x + a >= 100)
        if F == False:
            flag = False
            break

    if flag == True:
        print(a)
        break
