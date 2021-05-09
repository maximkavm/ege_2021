a = [0]*100
a[1] = 1
for i in range(2, 20):
    a[i] = a[i-1]
    a[i] += a[i-3]
    if a[i] // i == i:
        a[i] += a[i ** 0.5]
print(a[19])