result = -1
for A in range(999999999):
    flag = True
    for x in range(999):
        for y in range(999):
            F = ((2 * x + y) != 70) or (x < y) or (A < x)
            if F == 0:
                flag = False

    if flag == True:
        print(A)