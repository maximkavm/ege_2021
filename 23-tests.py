def num(s, x):
    if s > x: # если есть задание где надо пропустить какое-то число, то добавляем or x == это число
        return 0
    if s == x:
        return 1
    return num(s + 1, x) + num(s * 2, x)

print(num(1, 10)*num(10, 20))