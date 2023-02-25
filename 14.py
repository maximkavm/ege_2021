def dec_to(number, base):
    s = ''
    while number > 0:
        if number % base <= 9:
            s = str(number % base) + s
        number //= base
    return s

for i in range(2, 100):
    num = dec_to(31, i)
    if len(num) >= 2 and num[-1] == '1' and num[-2] == '1':
        print(i)