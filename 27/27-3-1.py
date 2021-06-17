f = open('27B-3-1.txt')
n = int(f.readline())
k10, k2, k5 = 0, 0, 0
for i in range(n):
    x = int(f.readline())
    if x % 10 == 0:
        k10 += 1
    elif x % 2 == 0:
        k2 += 1
    elif x % 5 == 0:
        k5 += 1
print(k10*(n-k10) + k2*k5 + (k10-1)//2*k10)