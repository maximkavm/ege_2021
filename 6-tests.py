def f(s):
    s = s // 10
    n = 1
    while s < 51:
        s = s + 5
        n = n * 2

    return n

for s in range(10000):
    if f(s) == 64:
        print(s)
