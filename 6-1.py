for s in range(-1000, 1000):
    n = 4
    while s < 37:
        s = s + 3
        n = n * 2
    if (n == 128):
        print(s)
        break