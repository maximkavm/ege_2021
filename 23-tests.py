def num(s, x):
    if s > x or s == 12: # если есть задание где надо пропустить какое-то число, то добавляем or s == это число
        return 0
    if s == x:
        return 1
    return num(s + 1, x) + num(s + 2, x) + num(s * 3, x)

print(num(2, 9)*num(9, 19))