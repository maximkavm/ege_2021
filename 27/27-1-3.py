f = open('27A-1-3.txt')
n = int(f.readline())
sum_f = 0
min_razn = 9999999999999
for i in range(n):
    a, b =map(int, f.readline().split())
    sum_f += min(a, b)
    if abs(a - b) < min_razn and abs(a - b) % 8 != 0:
        min_razn = abs(a - b)
if sum_f % 8 == 3:
    print(sum_f + min_razn)
else:
    print(sum_f)