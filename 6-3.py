for i in range(-1000, 1000):
    s = i
    n = 3
    while s < 220:
        s = s + 6
        n = n + 3
    if n > 40:
        print(i)