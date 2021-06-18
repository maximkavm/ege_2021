f = open('27-A_1.txt')
n = int(f.readline())
min_z = 10000000001
sum_f = 0
for i in range(n):
    a, b = map(int, f.readline().split())
    sum_f += max(a, b)
    if abs(a - b) < min_z and abs(a - b) % 3 != 0:
        min_z = abs(a - b)
if sum_f % 3 == 0:
    print(sum_f - min_z)
else:
    print(sum_f)