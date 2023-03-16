for i in range(1000):
    n = i
    r = bin(n)[2:]

    if r.count('1') % 2 == 0:
        r += '0'
        r = '10' + r[2:]
    else:
        r += '1'
        r = '11' + r[2:]

    if int(r, 2) > 40:
        print(n)
        break