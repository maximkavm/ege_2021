def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * F(n - 1) + G(n - 1) - n + 7

def G(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n - 1) + 3 * G(n - 1) - 2*n

print(F(14) + G(14))