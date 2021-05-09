def decto(x, base):
    s = ''
    while x:
        s = str(x % base) + s
        x //= base 

    return s

n = 9**7 + 3**8 - 5
print(decto(n, 3))
