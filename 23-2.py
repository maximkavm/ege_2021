def num(s, x):
    if s > x or s == 10:
        return 0
    if s == x:
        return 1
    return num(s + 1, x) + num(s * 2, x)
print(num(1, 25)*num(25, 28))