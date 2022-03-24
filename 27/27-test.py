def decto(x, base):
    s = ''
    while x > 0:
        s = str(x % base) + s
        x //= base
    return s

f = open('27A-1-1.txt')
n = int(f.readline())
sum_f = 0
max_razn = 999999999999
for i in range(n):
    a, b = map(int, f.readline().split())
    sum_f += min(a, b)
    if abs(a - b) < max_razn and int(decto(abs(a - b), 8)) % 3 != 0:
        max_razn = abs(a - b)

if int(decto(sum_f, 8)) % 3 == 0:
    print(sum_f - max_razn)
else:
    print(sum_f)