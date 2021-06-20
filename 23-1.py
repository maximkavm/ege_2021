def num(s, x):
    if x < s:
        return 0
    if x == s:
        return 1
    return num(s + 3, x) + num(s * 3, x)
print(num(5,27))