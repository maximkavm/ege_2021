for i in range(1, 1000):
    d = i
    s = 0
    n = 0
    while n < 200:
        s = s + 64
        n = n + d
    #print(s)
    if s == 192:
        print(d)