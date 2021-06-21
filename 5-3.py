def decto(x, base):
    s = ''
    while x:
        s = str(x % base) + s
        x //= base
    return s


def change(n):
    s = decto(n, 2)
    s += s[-1]
    if s.count('1') % 2 == 0:
        s = s + '0'
    else:
        s = s + '1'
    if s.count('1') % 2 == 0:
        s = s + '0'
    else:
        s = s + '1'
    n = int(s, base=2)
    return n


for i in range(1, 100):
    if change(i) > 130:
        print(i, change(i))