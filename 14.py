def decto(x, base):
    s = ''
    while x:
        s = str(x % base) + s
        x //= base 
    return s

n = 4**590 + 8**350 - 2**1020 - 25
print(decto(n, 2).count('0'))
