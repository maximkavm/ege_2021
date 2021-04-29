def decto(x, base):
    s = ''
    while x:
        s = str(x % base) + s
        x //= base 

    return s


for x in range(1000):
    n = 125**7 - 25**4 + x
    s = decto(n, 5)
    if s.count('4') == 15 and s.count('3') == 1 and s.count('1') == 2:
        print(x)
        break