def deli(n, m):
    if n % m == 0:
        return True
    else:
        return False

def f(x, A):
    F1 = deli(x, 2)
    F2 = not deli(x, 3)
    F3 = ((x + A) >= 100)
    return (F1 <= F2) or F3

for A in range(1000):
    flag = True
    for x in range(1000):
        if not f(x, A):
            flag = False

    if flag == True:
        print(A)
        break

