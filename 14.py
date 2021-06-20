def decto(x, base):
    s = ''
    while x:
        s = str(x % base) + s
        x //= base 
    return s

n = 9**8 + 3**24 - 18
print(decto(n, 3).count('2'))
