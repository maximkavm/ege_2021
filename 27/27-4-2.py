f = open('27A-4-2.txt')
n = int(f.readline())
sum_f = 0
min_razn = 9999999999999
for i in range(n):
    x, y, z = map(int, f.readline().split())
    a = [x, y, z]
    a.sort(reverse=True)
    sum_f += a[0]
    if (a[0] - a[1]) < min_razn and (a[0] - a[1]) % 5 != 0:
        min_razn = a[0] - a[1]
    if (a[0] - a[2]) < min_razn and (a[0] - a[2]) % 5 != 0:
        min_razn = a[0] - a[2]
if sum_f % 5 == 0:
    print(sum_f - min_razn)
else:
    print(sum_f)