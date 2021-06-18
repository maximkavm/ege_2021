f = open('27-10b.txt')
n = int(f.readline())
min_z = 10000000001
sum_f = 0
for i in range(n):
    a, b, c = map(int, f.readline().split())
    x = [a, b, c]
    x.sort(reverse=True)
    sum_f += x[0]
    if x[0] - x[1] < min_z and x[0] - x[1] % 4 != 0:
        min_z = x[0] - x[1]
    if x[0] - x[2] < min_z and x[0] - x[2] % 4 != 0:
        min_z = x[0] - x[2]
if sum_f % 4 == 0:
    print(sum_f - min_z)
else:
    print(sum_f)