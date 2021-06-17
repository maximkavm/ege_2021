f = open('27A-2-3.txt')
n = int(f.readline())
mx = 0
sum_sq_mx = 0
interval = []
for i in range(5):
    interval.append(int(f.readline()))
for i in range(n - 5):
    x = int(f.readline())
    if interval[0] > mx:
        mx = interval[0]
    if mx**2 + x**2 > sum_sq_mx:
        sum_sq_mx = mx**2 + x**2
    for j in range(4):
        interval[j] = interval[j+1]
    interval[4] = x
print(sum_sq_mx)
    
    

