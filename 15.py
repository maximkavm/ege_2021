def deli(n, m):
    if n % m == 0:
        return True
    else:
        return False

for a in range(1, 1000):
    b = True
    for x in range(0, 1000):
        F = ((deli(x, a) & deli(x, 24) & (not deli(x, 16))) <= (not deli(x, a)))
        if F == 0:
            b = False 
    if b == True:
        print(a)
