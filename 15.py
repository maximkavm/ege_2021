def deli(n, m):
    if n % m == 0:
        return True
    else:
        return False

for A in range(1, 1000000):
    b = True
    for x in range(0, 1000):
        F1 = not deli(x, 18)
        F2 = not deli(x, A)
        F3 = not deli(x, 12)
        F = F1 <= (F2 <= F3)
        if F == 0:
            b = False 
    if b == True:
        print(A)
