def decto(x, base):
    s = ""
    while x > 0:
        s = str(x % base) + s
        x //= base
    return s

def change(n):
    s = decto(n, 2)
    p = str(s.count('1') % 2)
    s = s + p
    p = str(s.count('1') % 2)
    s = s + p
    return int(s, base=2)

for i in range (100):
    if change(i) > 77:
        print(i)