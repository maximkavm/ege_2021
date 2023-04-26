count = 0
for n in range(1000, 10000):
    r = str(n)
    if int(r[0]) % 4 == 0:
        r = '9' + r[1:]
    if int(r[0]) % 2 == 0 and int(r[0]) % 4 != 0:
        r = '3' + r[1:]

    if r[0] == '9' and oct(int(r))[-1] == '4':
        count += 1

print(count)