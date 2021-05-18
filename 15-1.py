for A in range(1000):
    b = True
    for x in range(1000):
        F = (x&A != 0) <= ((x&10 == 0) <= (x&3 != 0))
        if F == 0:
            b = False
    if b == True:
        print(A)
