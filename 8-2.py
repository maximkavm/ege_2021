def decto(x, base):
    s = ''
    while x:
        s = str(x % base) + s
        x //= base
    return s

print(decto(1500, 4))