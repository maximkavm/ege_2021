def decto(x, base):
    s = ''
    while x:
        s = str(x % base) + s
        x //= base 

    return s

n = 9**5 + 3**25 - 20
print(decto(n, 3))
