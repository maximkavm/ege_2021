def decto(x, base):
    s = ''
    while x:
        s = str(x % base) + s
        x //= base 

    return s

sum = 0
cnt = 0
for i in range(697, 3459):
    if hex(i)[-1] == 'e' and decto(i, 7)[-1] == oct(i)[-1]:
        sum += i
        cnt += 1
print(sum, cnt)