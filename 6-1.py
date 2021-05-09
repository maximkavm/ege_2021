for s in range(-1000, 1000):
    n = 1
    while s < 208:
        s = s + 20
        n = n * 2
    if (n == 256):
        print(s)
