def deli(n, m):
    if n % m == 0:
        return True
    else:
        return False

for A in range(1, 1000):
    b = True
    for x in range(0, 1000):
        F = (deli(x, A) and (not deli(x, 36))) <= (not deli(x, 12))
        if F == 0:
            b = False 
    if b == True:
        print(A)
