def dec_to_bin(n):
    s = ""
    while n > 0:
        if n % 2 == 0:
            s += "0"
        else:
            s += "1"

        n //= 2

    return "".join(reversed(s))

def decto(n, base):
    s = ''
    while n > 0:
        s = str(n % base) + s
        n //= base

    return s

def change(s):

    if s.count("1") % 2 == 0:
        s += "0"
    else:
        s += "1"

    return s



for i in range(100):
    n = dec_to_bin(i)
    if int(change(change(n)), 2) > 77:
        print(i)



