def dec_to_bin(n):
    s = ''
    while n:
        if n % 2:
            s = '1' + s
        else:
            s = '0' + s
        n //= 2
    return s

def change(s):
    if s.count('1') % 2:
        s += '1'
    else:
        s += '0'
    return s


for i in range(100):
    n = int(change(change(dec_to_bin(i))), 2)
    if n > 77:
        print(i)
        break