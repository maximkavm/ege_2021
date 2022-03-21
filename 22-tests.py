for i in range(100000):
    X = i
    Q = 9
    L = 0
    while X >= Q:
        L = L + 1
        X = X - Q
    M = X
    if M < L:
        M = L
        L = X

    if L == 4 and M == 5:
        print(i)
