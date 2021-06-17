f = open('27A-1-1.txt')
n = int(f.readline())
sum_f = 0
min_razn = 9999999999999
for i in range(n):
    a, b =map(int, f.readline().split())
    sum_f += max(a, b)
    if abs(a - b) < min_razn and abs(a - b) % 4 != 0:
        min_razn = abs(a - b)
if sum_f % 4 == 0:
    print(sum_f - min_razn)
else:
    print(sum_f)