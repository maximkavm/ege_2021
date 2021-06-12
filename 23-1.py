def num(s, x):
    if x < s:
        return 0
    if x == s:
        return 1
    return num(s + 1, x) + num(s + 3, x) + num(s * 4, x)
print(num(1,18))