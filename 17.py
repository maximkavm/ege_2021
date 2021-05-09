def decto(x, base):
    s = ''
    while x:
        s = str(x % base) + s
        x //= base 

    return s

mx = 0
cnt = 0
for i in range(1016, 7937):
    if i % 3 == 0 and i % 7 != 0 and i % 17 != 0 and i % 19 != 0 and i % 27 != 0:
        cnt += 1
        if mx < i:
            mx = i
print(cnt, mx)