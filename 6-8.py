for i in range(-1000, 1000):
    s = i
    n = 127
    while s - n > 0:
        s = s + 15
        n = n + 20
    if s >= 1000:
        print(i)

