def F(n):
    if n <= 1:
        return 1
    if n % 2 == 0 and n > 1:
        return n * F(n - 1)
    elif n % 2 == 1 and n > 1:
        return n + F(n - 2)

print(F(84))
