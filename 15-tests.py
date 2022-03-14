def deli(n, m):
    if n % m == 0:
        return True
    else:
        return False

for A in range(1, 1000000000):
    flag = True
    for x in range(1, 100000):
        F1 = not deli(x, A)
        F2 = deli(x, 6)
        F3 = not deli(x, 9)
        F = F1 <= (F2 <= F3)

        if F == 0:
            flag = False
            break

    if flag == True:
        print(A)

