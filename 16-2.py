def F(n):
    if n == 1:
        return 3
    else:
        return 2 * F(n - 1) - n + 1

print(F(22))