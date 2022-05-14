def deli(n, m):
    if n % m == 0:
        return True
    else:
        return False

def F(A, x):
    F1 = deli(x, 3)
    F2 = not deli(x, 5)
    F3 = ((x + A) >= 70)
    return (F1 <= F2) + F3

for A in range(1, 1000):
    if all(F(A, x) for x in range(1, 1000)):
        print(A)