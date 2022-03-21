def decto(x, base):
    s = ''
    while x > 0:
        s = str(x % base) + s
        x //= base
    return s

n = 49**7 + 7**21 - 7
print(decto(n, 7).count('6'))
